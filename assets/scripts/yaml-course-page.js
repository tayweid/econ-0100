(function () {
    'use strict';

    const page = document.querySelector('[data-course-part]');
    if (!page) return;
    page.setAttribute('aria-busy', 'true');

    const partId = page.dataset.coursePart;
    const source = page.dataset.courseSource || 'course-content.yml';
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

    function pathThumbnail(video) {
        if (!video) return null;
        const link = element('a', 'path-thumb');
        link.href = `https://www.youtube.com/watch?v=${video}`;
        link.target = '_blank';
        link.rel = 'noopener';
        const image = element('img');
        image.src = thumbnail(video);
        image.alt = '';
        link.append(image);
        return link;
    }

    function pathStep({ name, where, links: stepLinks = [], date, due, video, classes = '', dotClasses = '' }) {
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
        const thumb = pathThumbnail(video);
        if (thumb) step.append(thumb);
        return step;
    }

    function extraStep(extra, bend) {
        return pathStep({
            name: extra.name,
            where: 'optional',
            links: items(extra.links),
            video: extra.video,
            classes: `path-step-alt ${bend ? 'path-step-bend' : 'path-step-extra'}`,
            dotClasses: 'path-dot-alt'
        });
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

    function explicitVignetteLinks(vignette, blockId) {
        const vignetteLinks = items(vignette.links).map(item => ({ ...item }));
        if (vignette.files) {
            const base = typeof vignette.files === 'string' ? vignette.files : blockId;
            vignetteLinks.push({ label: 'Vignette', file: `Vignettes/Vignette_${base}.pdf` });
            if (vignette.solutions === true) {
                vignetteLinks.push({
                    label: 'Solutions',
                    file: vignette.solution_file || `Vignettes/Vignette_${base}_sols.pdf`
                });
            }
        }
        return vignetteLinks;
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
        const homeworkLinks = [];
        if (homework.file) homeworkLinks.push({ label: 'Homework', file: `Homework/HW_${homework.file}.pdf` });
        if (homework.solutions === true) {
            const base = homework.solution_file || homework.file;
            homeworkLinks.push({ label: 'Solutions', file: `Homework/HW_${base}_sols.pdf` });
        }

        const due = dates.homework ? shortDate(dates.homework) : homework.due;
        const standard = [
            {
                date: dates.class,
                index: 0,
                node: pathStep({
                    name: exercise.name || `Exercise ${blockId}`,
                    where: 'in class',
                    links: items(exercise.links),
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
                    links: explicitVignetteLinks(vignette, blockId),
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
        container.replaceChildren();
        container.append(element('h1', 'title title-tight', `Part ${partId} | ${part.title}`));

        const tagline = String(part.tagline || '');
        container.append(element('i', 'subtitle-text', tagline.charAt(0).toUpperCase() + tagline.slice(1)));
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
        const blocks = new Map(sections.filter(section => section.block).map(section => [section.block, section]));
        const slots = Array.from(page.querySelectorAll('[data-course-block]'));
        const slotIds = slots.map(slot => slot.dataset.courseBlock);
        const blockIds = Array.from(blocks.keys());
        if (slotIds.join('|') !== blockIds.join('|')) {
            throw new Error(`The Part ${partId} HTML block shells (${slotIds.join(', ')}) do not match the YAML (${blockIds.join(', ')}).`);
        }

        renderDescription(page.querySelector('[data-course-description]'), part);
        slots.forEach(slot => renderBlock(slot, part, blocks.get(slot.dataset.courseBlock)));

        const checkpoint = sections.find(section => section.checkpoint);
        const checkpointSlot = page.querySelector('[data-course-checkpoint]');
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
            if (page.dataset.courseFallback) {
                const fallback = element('a', null, 'Open the standard page.');
                fallback.href = page.dataset.courseFallback;
                message.append(document.createTextNode(' '), fallback);
            }
        }
        console.error(error);
    }

    async function load() {
        try {
            if (!window.jsyaml || typeof window.jsyaml.load !== 'function') {
                throw new Error('The YAML reader did not load.');
            }
            const response = await fetch(source, { cache: 'no-cache' });
            if (!response.ok) throw new Error(`${source} returned ${response.status}.`);
            const data = window.jsyaml.load(await response.text());
            const part = data && data.parts && data.parts[partId];
            if (!part) throw new Error(`Part ${partId} is missing from ${source}.`);

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
