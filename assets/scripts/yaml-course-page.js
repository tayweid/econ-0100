(function () {
    'use strict';

    const page = document.querySelector('[data-course-part]');
    if (!page) return;
    page.setAttribute('aria-busy', 'true');

    const partId = page.dataset.coursePart;
    const source = 'course-content.yaml.js';
    let discoveredFiles = {};
    let courseScriptInitialized = false;
    document.addEventListener('DOMContentLoaded', () => {
        courseScriptInitialized = true;
    }, { once: true });

    function element(tag, className, text) {
        const node = document.createElement(tag);
        if (className) node.className = className;
        if (text !== undefined && text !== null) node.textContent = String(text);
        return node;
    }

    function items(value) {
        return Array.isArray(value) ? value : [];
    }

    function appendInlineText(node, value, stripOuterEmphasis) {
        let text = String(value || '');
        if (stripOuterEmphasis && /^\*[^*]+\*$/.test(text)) text = text.slice(1, -1);

        const expression = /\*([^*]+)\*/g;
        let cursor = 0;
        let match;
        while ((match = expression.exec(text))) {
            node.append(document.createTextNode(text.slice(cursor, match.index)));
            node.append(element('i', null, match[1]));
            cursor = match.index + match[0].length;
        }
        node.append(document.createTextNode(text.slice(cursor)));
    }

    function thumbnail(video) {
        return `https://img.youtube.com/vi/${video}/maxresdefault.jpg`;
    }

    function resourceLink(item) {
        const href = String(item.file);
        const optional = Boolean(item.optional);
        let icon = item.icon;
        let className;

        if (item.label === 'Practice') {
            icon ||= 'fa fa-pencil';
            className = 'practice-link';
        } else if (/^https?:/i.test(href)) {
            icon ||= 'fa fa-external-link';
            className = 'download-link';
        } else {
            icon ||= 'fa fa-file-pdf-o';
            className = 'download-link';
        }
        if (optional) className += ' chip-optional';

        const link = element('a', className);
        link.href = href;
        link.target = '_blank';
        link.rel = 'noopener';
        const iconNode = element('i', icon);
        iconNode.setAttribute('aria-hidden', 'true');
        link.append(iconNode, document.createTextNode(` ${item.label}${optional ? ' · optional' : ''}`));
        return link;
    }

    function links(itemsToRender) {
        if (!itemsToRender.length) return null;
        const container = element('div', 'path-links');
        itemsToRender.forEach(item => container.append(resourceLink(item)));
        return container;
    }

    function shortDate(iso) {
        const date = new Date(`${iso}T00:00:00Z`);
        if (Number.isNaN(date.getTime())) return String(iso);
        return new Intl.DateTimeFormat('en-US', {
            weekday: 'short',
            month: 'short',
            day: 'numeric',
            timeZone: 'UTC'
        }).format(date).replace(',', '');
    }

    // The small thumbnail beside a step: a YouTube frame when the step has a video,
    // otherwise an image the YAML names (a podcast's episode art, say) linking to the
    // step's first link.
    function pathThumbnail(video, image, href) {
        if (!video && !(image && href)) return null;
        const link = element('a', 'path-thumb');
        link.href = video ? `https://www.youtube.com/watch?v=${video}` : href;
        link.target = '_blank';
        link.rel = 'noopener';
        const imageNode = element('img');
        imageNode.src = video ? thumbnail(video) : String(image);
        imageNode.alt = '';
        link.append(imageNode);
        return link;
    }

    function pathStep({ name, where, links: stepLinks = [], date, due, video, image, classes = '', dotClasses = '' }) {
        const step = element('li', `path-step${classes ? ` ${classes}` : ''}`);
        if (date) step.dataset.date = date;

        const dot = element('span', `path-dot${dotClasses ? ` ${dotClasses}` : ''}`);
        dot.setAttribute('aria-hidden', 'true');
        const body = element('div');
        const title = element('p', 'path-name');
        title.append(document.createTextNode(`${name} `), element('span', 'path-where', where));
        body.append(title);

        const renderedLinks = links(stepLinks);
        if (renderedLinks) body.append(renderedLinks);
        if (due) body.append(element('p', 'path-due', due));

        step.append(dot, body);
        const thumb = pathThumbnail(video, image, stepLinks.length ? String(stepLinks[0].file) : null);
        if (thumb) step.append(thumb);
        return step;
    }

    function extraStep(extra, bend) {
        const step = pathStep({
            name: extra.name,
            where: 'optional',
            links: items(extra.links),
            video: extra.video,
            image: extra.image,
            classes: `path-step-alt ${bend ? 'path-step-bend' : 'path-step-extra'}`,
            dotClasses: 'path-dot-alt'
        });
        if (extra.video) step.dataset.videoId = extra.video;
        return step;
    }

    function videoPanel(name, video) {
        const cardVideo = element('div', 'card-video');
        const image = element('img');
        if (video) {
            image.src = thumbnail(video);
            image.alt = `${name} thumbnail`;
            cardVideo.append(image, element('div', 'play-button', '▶'));
        } else {
            image.alt = '';
            image.className = 'placeholder-bg';
            cardVideo.append(image);
        }
        return cardVideo;
    }

    function episodePanel(blockId, block) {
        const episode = block.episode || {};
        const reading = block.reading || {};
        const name = episode.name || `Episode ${blockId}`;
        const panel = element('div', 'path-episode');
        if (episode.video) panel.dataset.videoId = episode.video;
        panel.append(videoPanel(name, episode.video));

        const title = element('p', 'path-name');
        title.append(document.createTextNode(`${name} `));
        const description = element('span', 'path-desc');
        appendInlineText(description, episode.description || '', true);
        title.append(description);
        panel.append(title);

        const episodeLinks = items(episode.links).map(item => ({ ...item }));
        if (reading.chapter && reading.file !== false) {
            const chapter = String(reading.chapter).padStart(2, '0');
            episodeLinks.push({
                label: `Ch. ${reading.chapter}`,
                file: typeof reading.file === 'string' ? reading.file : `Reading/Ch_${chapter}.pdf`,
                optional: true
            });
        } else if (reading.name) {
            episodeLinks.push(...items(reading.links).map(item => ({ ...item })));
        }

        const renderedLinks = links(episodeLinks);
        if (renderedLinks) panel.append(renderedLinks);
        return panel;
    }

    // Conventional per-block files, the same shape scripts/check-course expects:
    // Blocks/<folder>/<Type>/<Type>_<base>[_sols].pdf. The folder slug is the only piece
    // a browser cannot derive, so the YAML carries it; existence is settled by asking
    // for the file, the runtime equivalent of Ruby's File.exist?.
    function explicitPath(value) {
        return typeof value === 'string' && value.includes('/');
    }

    function conventionalPath(folder, type, base, suffix) {
        const name = [type, base, suffix].filter(Boolean).join('_');
        return `Blocks/${folder}/${type}/${name}.pdf`;
    }

    // A page opened from disk has an opaque origin where every fetch is refused, but the
    // browser still lets it load a neighbouring <link> or <script>, and those fire load or
    // error according to whether the file is there. A stylesheet link is the quiet way to
    // ask: nothing is executed, and the element is removed the moment it answers.
    function existsOnDisk(path) {
        return new Promise(resolve => {
            const probe = document.createElement('link');
            probe.rel = 'stylesheet';
            probe.onload = () => { probe.remove(); resolve(true); };
            probe.onerror = () => { probe.remove(); resolve(false); };
            probe.href = path;
            document.head.append(probe);
        });
    }

    // Served over http(s) a HEAD request answers directly and sees exactly what is
    // published. From disk the link probe above stands in for it.
    async function exists(path) {
        if (location.protocol === 'file:') return existsOnDisk(path);
        for (let attempt = 0; attempt < 2; attempt += 1) {
            try {
                return (await fetch(path, { method: 'HEAD' })).ok;
            } catch (error) {
                // A rejected fetch is a transport fault, not a 404; give it one more try.
            }
        }
        return false;
    }

    function blockCandidates(section) {
        const blockId = section.block;
        const folder = section.folder;
        if (!blockId || !folder || section.steps) return [];
        const wanted = [];

        // Exercise and vignette are discovered whether or not the YAML names them --
        // the generator stats these paths for every block, so the runtime must too.
        const exercise = section.exercise || {};
        if (!exercise.links) {
            wanted.push(['exercise', conventionalPath(folder, 'Exercise', blockId)]);
        }

        const homework = section.homework || {};
        if (!homework.links) {
            if (homework.file && !explicitPath(homework.file)) {
                wanted.push(['homework', conventionalPath(folder, 'Homework', blockId)]);
            }
            // Opt-in, not opt-out: a solutions PDF merely sitting on disk must never
            // put a link on the public site. Same rule the generator enforces.
            if (homework.solutions === true && !explicitPath(homework.solution_file)) {
                wanted.push(['homework_sols', conventionalPath(folder, 'Homework', blockId, 'sols')]);
            }
        }

        const vignette = section.vignette || {};
        if (!vignette.links && vignette.files !== false) {
            const base = typeof vignette.files === 'string' ? vignette.files : blockId;
            if (!explicitPath(base)) {
                wanted.push(['vignette', conventionalPath(folder, 'Vignette', base)]);
                if (vignette.solutions === true) {
                    wanted.push(['vignette_sols', conventionalPath(folder, 'Vignette', base, 'sols')]);
                }
            }
        }
        return wanted;
    }

    async function discoverBlockFiles(part) {
        const probes = [];
        items(part.sections).forEach(section => {
            blockCandidates(section).forEach(([key, path]) => {
                probes.push(exists(path).then(ok => ({ block: section.block, key, path, ok })));
            });
        });
        const found = {};
        (await Promise.all(probes)).forEach(result => {
            if (result.ok) (found[result.block] ||= {})[result.key] = result.path;
        });
        return found;
    }

    function vignetteLinks(vignette, blockFiles) {
        if (vignette.links) return items(vignette.links).map(item => ({ ...item }));
        if (vignette.files === false) return [];
        const found = [];
        if (blockFiles.vignette) found.push({ label: 'Vignette', file: blockFiles.vignette });
        if (vignette.solutions === true && blockFiles.vignette_sols) {
            found.push({ label: 'Solutions', file: blockFiles.vignette_sols });
        }
        return found;
    }

    function blockSteps(part, block) {
        const blockId = block.block;
        const extras = items(block.extras).map(extra => extraStep(extra, false));

        if (block.steps) {
            return extras.concat(items(block.steps).map(step => pathStep({
                name: step.name,
                where: step.where || 'home',
                links: items(step.links),
                date: step.date,
                due: step.due ? `Due ${step.due}` : null,
                video: step.video
            })));
        }

        const dates = block.dates || {};
        const exercise = block.exercise || {};
        const vignette = block.vignette || {};
        const homework = { ...(part.homework_defaults || {}), ...(block.homework || {}) };
        const blockFiles = discoveredFiles[blockId] || {};
        const homeworkLinks = [];
        if (homework.links) {
            homeworkLinks.push(...items(homework.links).map(item => ({ ...item })));
        } else {
            const file = explicitPath(homework.file) ? homework.file : blockFiles.homework;
            if (homework.file && file) homeworkLinks.push({ label: 'Homework', file });
            if (homework.solutions === true) {
                const sols = explicitPath(homework.solution_file) ? homework.solution_file : blockFiles.homework_sols;
                if (sols) homeworkLinks.push({ label: 'Solutions', file: sols });
            }
        }

        const due = dates.homework ? shortDate(dates.homework) : homework.due;
        const standard = [
            {
                date: dates.class,
                index: 0,
                node: pathStep({
                    name: exercise.name || `Exercise ${blockId}`,
                    where: 'in class',
                    links: exercise.links ? items(exercise.links)
                        : (blockFiles.exercise ? [{ label: 'Exercise', file: blockFiles.exercise }] : []),
                    date: dates.class,
                    video: exercise.video
                })
            },
            {
                date: dates.recitation,
                index: 1,
                node: pathStep({
                    name: vignette.name || `Vignette ${blockId}`,
                    where: 'recitation',
                    links: vignetteLinks(vignette, blockFiles),
                    date: dates.recitation,
                    video: vignette.video
                })
            },
            {
                date: dates.homework,
                index: 2,
                node: pathStep({
                    name: `Homework ${blockId}`,
                    where: 'home',
                    links: homeworkLinks,
                    date: dates.homework,
                    due: due ? `Due ${due}` : null,
                    video: homework.video
                })
            }
        ];

        if (standard.every(step => step.date)) {
            standard.sort((left, right) => left.date.localeCompare(right.date) || left.index - right.index);
        }
        return extras.concat(standard.map(step => step.node));
    }

    function renderBlock(slot, part, block) {
        slot.hidden = false;
        slot.className = 'block';
        slot.replaceChildren();
        slot.append(
            element('h1', 'subtitle', `Block ${block.block} | ${block.title}`),
            element('p', 'block-description', block.description)
        );

        const path = element('div', `path${block.practice === false ? ' path-solo' : ''}`);
        path.append(episodePanel(block.block, block));
        if (block.practice !== false) {
            const steps = element('ol', 'path-steps');
            blockSteps(part, block).forEach(step => steps.append(step));
            path.append(steps);
        }
        slot.append(path);
    }

    function renderCheckpoint(slot, config) {
        const demo = config.demo || {};
        slot.hidden = false;
        slot.className = 'block checkpoint';
        slot.replaceChildren();
        slot.append(element('h1', 'subtitle', `Checkpoint ${partId}`));

        const description = element('p', 'block-description');
        appendInlineText(description, config.description || '');
        slot.append(description);

        const path = element('div', 'path');
        const episode = element('div', 'path-episode');
        if (demo.video) episode.dataset.videoId = demo.video;
        episode.append(videoPanel(`Demo ${partId}`, demo.video));

        const episodeName = element('p', 'path-name');
        episodeName.append(document.createTextNode(`Demo ${partId} Walkthrough `));
        const walkthrough = element('span', 'path-desc');
        appendInlineText(
            walkthrough,
            demo.description || `Attempt Demo ${partId} first, then walk through with me.`,
            true
        );
        episodeName.append(walkthrough);
        episode.append(episodeName);
        path.append(episode);

        const steps = element('ol', 'path-steps path-checkpoint');
        steps.append(pathStep({
            name: `Demo ${partId}`,
            where: 'home',
            links: items(demo.links)
        }));

        const extras = items(config.extras);
        extras.forEach((extra, index) => steps.append(extraStep(extra, index === 0)));
        steps.append(pathStep({
            name: `Checkpoint ${partId}`,
            where: 'in class',
            date: config.date,
            due: config.when || (config.date ? shortDate(config.date) : null),
            classes: `path-step-checkpoint${extras.length ? ' path-step-cont' : ''}`,
            dotClasses: 'path-dot-big'
        }));
        steps.append(pathStep({
            name: 'Reattempt',
            where: config.reattempt || 'TBA',
            classes: 'path-step-alt',
            dotClasses: 'path-dot-alt'
        }));
        path.append(steps);
        slot.append(path);
    }

    function renderDescription(container, part) {
        const errorMessage = container.querySelector('[data-course-error]');
        container.replaceChildren();
        container.append(element('h1', 'title title-tight', `Part ${partId} | ${part.title}`));

        const tagline = String(part.tagline || '');
        container.append(element('i', 'subtitle-text', tagline.charAt(0).toUpperCase() + tagline.slice(1)));
        if (errorMessage) container.append(errorMessage);
        items(part.links).forEach(item => container.append(document.createTextNode(' '), resourceLink(item)));
        container.append(element('hr', 'title-rule'), element('p', null, part.introduction));
    }

    function updatePageNavigation(sections) {
        const navigation = document.querySelector('[data-course-page-nav]');
        if (!navigation) return;
        const blocks = new Map(sections.filter(section => section.block).map(section => [section.block, section]));
        navigation.querySelectorAll('[data-nav-block]').forEach(link => {
            const block = blocks.get(link.dataset.navBlock);
            if (block) link.textContent = `${block.block} | ${block.nav}`;
        });
    }

    function renderPart(part) {
        const sections = items(part.sections);
        const unsupported = sections.filter(section => !section.block && !section.checkpoint);
        if (unsupported.length) throw new Error(`Part ${partId} contains a section type this runtime does not support.`);

        const blockSections = sections.filter(section => section.block);
        const blockIds = blockSections.map(section => section.block);
        if (new Set(blockIds).size !== blockIds.length) {
            throw new Error(`Part ${partId} contains duplicate block IDs.`);
        }
        const checkpoints = sections.filter(section => section.checkpoint);
        if (checkpoints.length > 1) throw new Error(`Part ${partId} contains more than one checkpoint.`);

        const blocks = new Map(blockSections.map(section => [section.block, section]));
        const slots = Array.from(page.querySelectorAll('[data-course-block]'));
        const slotIds = slots.map(slot => slot.dataset.courseBlock);
        if (slotIds.join('|') !== blockIds.join('|')) {
            throw new Error(`The Part ${partId} HTML block shells (${slotIds.join(', ')}) do not match the YAML (${blockIds.join(', ')}).`);
        }
        const expectedElementIds = blockIds.map(blockId => `part-${blockId.toLowerCase()}`);
        const actualElementIds = slots.map(slot => slot.id);
        if (actualElementIds.join('|') !== expectedElementIds.join('|')) {
            throw new Error(`The Part ${partId} HTML block IDs (${actualElementIds.join(', ')}) should be ${expectedElementIds.join(', ')}.`);
        }

        const checkpoint = checkpoints[0];
        const checkpointSlot = page.querySelector('[data-course-checkpoint]');
        if (Boolean(checkpoint) !== Boolean(checkpointSlot) || (checkpointSlot && checkpointSlot.id !== 'checkpoint')) {
            throw new Error(`The Part ${partId} checkpoint shell does not match the YAML.`);
        }

        const pageNavigation = document.querySelector('[data-course-page-nav]');
        const actualNavigation = pageNavigation
            ? Array.from(pageNavigation.querySelectorAll('.nav-link-right')).map(link => ({
                href: link.getAttribute('href'),
                block: link.dataset.navBlock || null
            }))
            : [];
        const expectedNavigation = blockIds.map((blockId, index) => ({
            href: `#${expectedElementIds[index]}`,
            block: blockId
        }));
        if (checkpoint) expectedNavigation.push({ href: '#checkpoint', block: null });
        if (JSON.stringify(actualNavigation) !== JSON.stringify(expectedNavigation)) {
            throw new Error(`The Part ${partId} right-navigation shell does not match the YAML.`);
        }

        renderDescription(page.querySelector('[data-course-description]'), part);
        slots.forEach(slot => renderBlock(slot, part, blocks.get(slot.dataset.courseBlock)));

        if (checkpoint && checkpointSlot) renderCheckpoint(checkpointSlot, checkpoint.checkpoint);
        else if (checkpointSlot) checkpointSlot.hidden = true;
        updatePageNavigation(sections);
    }

    function initializeLateContent() {
        [
            'setupCarousels',
            'setupVideoCards',
            'setupActiveCardHighlighting',
            'setupTopicToggles',
            'setupPathDates'
        ].forEach(name => {
            if (typeof window[name] === 'function') window[name]();
        });
    }

    function showError(error) {
        page.removeAttribute('aria-busy');
        const message = page.querySelector('[data-course-error]');
        if (message) {
            message.hidden = false;
            message.replaceChildren(document.createTextNode(`The course content could not be loaded. ${error.message}`));
        }
        console.error(error);
    }

    // course-content.yaml.js is a <script> that assigns the YAML to a global. Loading a
    // neighbouring script is the one thing a page opened straight from the filesystem is
    // allowed to do, and it works identically when served, so there is no fetch and no
    // second copy of the content to fall out of date.
    function readSource() {
        if (typeof window.COURSE_CONTENT_YAML !== 'string') {
            throw new Error(`${source} did not load.`);
        }
        return window.COURSE_CONTENT_YAML;
    }

    async function load() {
        try {
            if (!window.jsyaml || typeof window.jsyaml.load !== 'function') {
                throw new Error('The YAML reader did not load.');
            }
            const data = window.jsyaml.load(readSource());
            const part = data && data.parts && data.parts[partId];
            if (!part) throw new Error(`Part ${partId} is missing from ${source}.`);

            discoveredFiles = await discoverBlockFiles(part);
            renderPart(part);
            page.removeAttribute('aria-busy');
            page.dataset.courseReady = 'true';
            if (window.performance && typeof window.performance.now === 'function') {
                page.dataset.courseLoadMs = String(Math.round(window.performance.now()));
            }
            if (courseScriptInitialized) initializeLateContent();

            if (location.hash) {
                requestAnimationFrame(() => {
                    const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
                    if (target) target.scrollIntoView();
                });
            }
            document.dispatchEvent(new CustomEvent('course-content-ready', {
                detail: { part: partId, loadMs: Number(page.dataset.courseLoadMs) || null }
            }));
        } catch (error) {
            showError(error);
        }
    }

    load();
}());
