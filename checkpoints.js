/* Course Logistics: dates come from course-content.yaml.js, just as on the Part pages.
 * Eligibility is cumulative by session name, not checkpoint date:
 * Reattempt A offers A; Reattempt B offers A+B, even when Checkpoint B precedes Reattempt A.
 */
(function () {
    'use strict';
    const assets = 'https://tayweid.github.io/course-assets/';
    const localAssets = '../tayweid.github.io/course-assets/';
    const svgNS = 'http://www.w3.org/2000/svg';
    const routeColor = 'var(--link)';

    function loadYaml() {
        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = (location.protocol === 'file:' ? localAssets : assets) + 'js-yaml.min.js';
            script.onload = resolve;
            script.onerror = () => {
                if (script.src.startsWith('file:')) {
                    script.onerror = reject;
                    script.src = assets + 'js-yaml.min.js';
                } else reject(new Error('Could not load the course schedule reader.'));
            };
            document.head.append(script);
        });
    }

    function dates(value) {
        return (Array.isArray(value) ? value : [value]).filter(date => typeof date === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(date));
    }

    function dateLabel(value) {
        const list = dates(value);
        if (!list.length) return 'Date TBA';
        const format = date => new Date(date + 'T12:00:00Z').toLocaleDateString('en-US', { month: 'short', day: 'numeric', timeZone: 'UTC' });
        if (list.length === 1) return format(list[0]);
        return list[0].slice(0, 7) === list[1].slice(0, 7)
            ? format(list[0]) + '–' + Number(list[1].slice(-2))
            : list.map(format).join(' / ');
    }

    function svgElement(tag, attributes, text) {
        const node = document.createElementNS(svgNS, tag);
        Object.entries(attributes || {}).forEach(([key, value]) => node.setAttribute(key, value));
        if (text !== undefined) node.textContent = text;
        return node;
    }

    function text(svg, x, y, value, className, anchor = 'middle') {
        svg.append(svgElement('text', { x, y, class: className, 'text-anchor': anchor }, value));
    }

    function eventMeta(parent, x, y, event, anchor = 'middle', stacked = false) {
        const line = svgElement('text', { x, y, class: 'event-date', 'text-anchor': anchor });
        line.append(document.createTextNode(dateLabel(event.date) + (stacked ? '' : ' · ')));
        line.append(svgElement('tspan', stacked ? { class: 'event-place', x, dy: 15 } : { class: 'event-place' }, event.place.toUpperCase()));
        parent.append(line);
    }

    function eventHeading(svg, shape, event) {
        if (event.detail) {
            return tipTarget(svg, shape, { title: event.name, body: event.detail });
        }
        const heading = svgElement('g');
        svg.append(heading);
        return heading;
    }

    function previousCheckpoint(events, first) {
        for (let index = first - 1; index >= 0; index--) {
            if (events[index].kind !== 'reattempt') return index;
        }
        return -1;
    }

    function practiceStart(svg, part, x, y, color) {
        svg.append(svgElement('circle', { cx: x, cy: y, r: 4.5, class: 'practice-start', 'data-part': part, stroke: color }));
    }

    let activeTip = null;
    let activeInfo = null;
    let pinnedTip = false;
    let hideTimer;

    function hideTip() {
        clearTimeout(hideTimer);
        if (activeTip) activeTip.removeAttribute('aria-describedby');
        activeTip = null;
        activeInfo = null;
        pinnedTip = false;
        document.getElementById('map-tooltip').hidden = true;
    }

    function showTip(trigger, info) {
        clearTimeout(hideTimer);
        if (activeTip !== trigger) hideTip();
        activeTip = trigger;
        activeInfo = info;
        const tip = document.getElementById('map-tooltip');
        const title = document.createElement('strong');
        title.textContent = info.title;
        const body = document.createElement('p');
        body.textContent = info.body;
        tip.replaceChildren(title, body);
        tip.hidden = false;
        trigger.setAttribute('aria-describedby', 'map-tooltip');
        const anchor = trigger.getBoundingClientRect();
        const bounds = tip.getBoundingClientRect();
        const left = Math.max(12, Math.min(anchor.left + anchor.width / 2 - bounds.width / 2, innerWidth - bounds.width - 12));
        const below = anchor.bottom + 10;
        const top = below + bounds.height <= innerHeight - 12 ? below : Math.max(12, anchor.top - bounds.height - 10);
        tip.style.left = left + 'px';
        tip.style.top = top + 'px';
    }

    function tipTarget(svg, shape, info, label = info.title) {
        const group = svgElement('g', { class: 'tip-target', role: 'button', tabindex: 0, 'aria-label': label });
        group.append(shape);
        group.addEventListener('pointerenter', event => {
            if (event.pointerType !== 'touch' && !pinnedTip) showTip(group, info);
        });
        group.addEventListener('pointerleave', () => {
            if (!pinnedTip && document.activeElement !== group) hideTimer = setTimeout(hideTip, 150);
        });
        group.addEventListener('focus', () => showTip(group, info));
        group.addEventListener('blur', hideTip);
        const toggle = () => {
            if (activeTip === group && pinnedTip) hideTip();
            else { showTip(group, info); pinnedTip = true; }
        };
        group.addEventListener('click', toggle);
        group.addEventListener('keydown', event => {
            if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); toggle(); }
        });
        svg.append(group);
        return group;
    }

    function buildSchedule(data) {
        const parts = Object.entries(data.parts).map(([id, part]) => ({
            id, checkpoint: part.sections.find(section => section.checkpoint)?.checkpoint
        })).filter(part => part.checkpoint);
        const events = [];
        parts.forEach((part, index) => {
            const cp = part.checkpoint;
            const final = part.id === 'F';
            if (dates(cp.date).length) events.push({
                id: 'checkpoint-' + part.id, part: part.id, kind: final ? 'final' : 'checkpoint',
                date: cp.date, name: final ? 'Final session' : 'Checkpoint ' + part.id,
                place: final ? 'See Canvas' : 'In class',
                detail: final && cp.when ? cp.when + '. Checkpoint F and reattempts for earlier parts.' : cp.when || null,
                // The syllabus promises a final reattempt session for earlier parts.
                available: final ? parts.slice(0, index).map(p => p.id) : [part.id]
            });
            if (dates(cp.reattempt_date).length) events.push({
                id: 'reattempt-' + part.id, part: part.id, kind: 'reattempt',
                date: cp.reattempt_date, name: 'Reattempt ' + part.id,
                place: cp.reattempt || 'See Canvas',
                detail: null,
                available: parts.slice(0, index + 1).map(p => p.id)
            });
        });
        events.sort((a, b) => dates(a.date)[0].localeCompare(dates(b.date)[0]) || a.id.localeCompare(b.id));
        return { parts, events };
    }

    function renderMap(schedule, full) {
        const parts = full ? schedule.parts : schedule.parts.filter(part => ['A', 'B'].includes(part.id));
        const events = full ? schedule.events : schedule.events.filter(event => ['A', 'B'].includes(event.part) && event.kind !== 'final');
        const width = full ? Math.max(1340, events.length * 126 + 80) : 830;
        hideTip();
        const rowGap = full ? 32 : 44;
        const firstRow = full ? 82 : 94;
        const height = firstRow + (parts.length - 1) * rowGap + 26;
        const start = full ? 126 : 148;
        const end = width - (full ? 66 : 135);
        const x = index => events.length > 1 ? start + index * (end - start) / (events.length - 1) : start;
        const svg = svgElement('svg', {
            viewBox: `0 0 ${width} ${height}`, class: 'route-map' + (full ? ' full' : ' example'),
            role: 'group', 'aria-labelledby': 'route-title', 'aria-describedby': 'route-desc'
        });
        svg.append(svgElement('title', { id: 'route-title' }, full ? 'The full checkpoint and reattempt timeline' : 'How Parts A and B continue through reattempts'));
        svg.append(svgElement('desc', { id: 'route-desc' }, events.map(event =>
            `${event.name}, ${dateLabel(event.date)}, ${event.place}: ${event.kind === 'final' ? 'Checkpoint F and reattempts for' : event.kind === 'checkpoint' ? 'first attempt for' : 'reattempts for'} Part${event.available.length > 1 ? 's' : ''} ${event.available.join(', ')}.`
        ).join(' ') + ' An open circle starts each part’s practice period at the preceding checkpoint. Part A starts before the first checkpoint. Solid paths lead to first attempts; dashed paths connect later chances. A vertical bar marks a checkpoint; a hollow diamond marks a reattempt.'));
        svg.append(svgElement('line', { x1: start - 38, y1: 59, x2: width - 30, y2: 59, class: 'axis' }));
        events.forEach((event, index) => {
            const at = x(index);
            const heading = eventHeading(svg, svgElement('rect', { x: at - (full ? 62 : 85), y: 0, width: full ? 124 : 170, height: 54, class: 'tip-hit' }), event);
            text(heading, at, 17, event.name, 'event-name');
            eventMeta(heading, at, full ? 34 : 39, event, 'middle', full);
            svg.append(svgElement('line', { x1: at, y1: 53, x2: at, y2: 65, class: 'axis' }));
            svg.append(svgElement('line', { x1: at, y1: 70, x2: at, y2: height - 15, class: 'guide-line' }));
        });
        parts.forEach((part, row) => {
            const y = firstRow + row * rowGap;
            const color = routeColor;
            text(svg, 14, y + 6, 'Part ' + part.id, 'part-label', 'start');
            const first = events.findIndex(event => event.part === part.id && event.kind !== 'reattempt');
            if (first < 0) return;
            const firstX = x(first);
            const previous = previousCheckpoint(events, first);
            const from = previous >= 0 ? x(previous) : firstX - 36;
            svg.append(svgElement('path', { d: `M ${from} ${y} H ${firstX}`, class: 'route practice-path', 'data-part': part.id, stroke: color }));
            practiceStart(svg, part.id, from, y, color);
            const chances = events.map((event, index) => ({ event, index })).filter(({ event, index }) =>
                index > first && event.kind !== 'checkpoint' && event.available.includes(part.id));
            if (chances.length || !full) {
                const lastX = full ? x(chances[chances.length - 1].index) : width - 29;
                svg.append(svgElement('path', { d: `M ${firstX} ${y} H ${lastX}`, class: 'route retry', stroke: color }));
                if (!full) {
                    svg.append(svgElement('path', { d: `M ${lastX - 7} ${y - 5} L ${lastX} ${y} L ${lastX - 7} ${y + 5}`, class: 'route', stroke: color }));
                    text(svg, width - 70, y - 15, 'and later', 'end-label');
                }
            }
            [first, ...chances.map(chance => chance.index)].forEach(index => {
                const at = x(index);
                // Remove a little connecting line around each tick for legibility.
                svg.append(svgElement('rect', { x: at - 6, y: y - 14, width: 12, height: 28, fill: 'var(--bg)' }));
                if (index === first) {
                    svg.append(svgElement('line', { x1: at, y1: y - 9, x2: at, y2: y + 9, class: 'stop', stroke: color }));
                } else {
                    svg.append(svgElement('path', { d: `M ${at} ${y - 8} L ${at + 6} ${y} L ${at} ${y + 8} L ${at - 6} ${y} Z`, class: 'reattempt-stop', stroke: color }));
                }
            });
        });
        const map = document.getElementById('timeline-map');
        map.replaceChildren(svg);
        if (!full) renderCompactMap(parts, events, svg.querySelector('desc').textContent);
    }

    // At phone widths, turn the A/B diagram so both routes and all four stops are
    // visible together. The desktop version preserves the horizontal timeline.
    function renderCompactMap(parts, events, description) {
        const height = 76 + events.length * 66;
        const svg = svgElement('svg', {
            viewBox: `0 0 350 ${height}`, class: 'route-map compact',
            role: 'group', 'aria-labelledby': 'compact-title', 'aria-describedby': 'compact-desc'
        });
        svg.append(svgElement('title', { id: 'compact-title' }, 'Follow Parts A and B down the timeline'));
        svg.append(svgElement('desc', { id: 'compact-desc' }, description.replace('A vertical bar', 'A horizontal bar')));
        const y = index => 64 + index * 66;
        events.forEach((event, index) => {
            const heading = eventHeading(svg, svgElement('rect', { x: 0, y: y(index) - 25, width: 175, height: 48, class: 'tip-hit' }), event);
            text(heading, 2, y(index) - 8, event.name, 'event-name', 'start');
            eventMeta(heading, 2, y(index) + 14, event, 'start');
            svg.append(svgElement('line', { x1: 158, y1: y(index), x2: 330, y2: y(index), class: 'guide-line' }));
        });
        parts.forEach((part, index) => {
            const x = 215 + index * 95;
            const color = routeColor;
            text(svg, x, 23, 'Part ' + part.id, 'part-label');
            const first = events.findIndex(event => event.part === part.id && event.kind === 'checkpoint');
            if (first < 0) return;
            const previous = previousCheckpoint(events, first);
            const from = previous >= 0 ? y(previous) : y(first) - 27;
            svg.append(svgElement('path', { d: `M ${x} ${from} V ${y(first)}`, class: 'route practice-path', 'data-part': part.id, stroke: color }));
            practiceStart(svg, part.id, x, from, color);
            svg.append(svgElement('path', { d: `M ${x} ${y(first)} V ${height - 47}`, class: 'route retry', stroke: color }));
            svg.append(svgElement('path', { d: `M ${x - 5} ${height - 54} L ${x} ${height - 47} L ${x + 5} ${height - 54}`, class: 'route', stroke: color }));
            text(svg, x, height - 19, 'and later', 'end-label');
            events.forEach((event, eventIndex) => {
                const initial = eventIndex === first;
                if (!initial && !(event.kind === 'reattempt' && event.available.includes(part.id))) return;
                svg.append(svgElement('rect', { x: x - 14, y: y(eventIndex) - 6, width: 28, height: 12, fill: 'var(--bg)' }));
                if (initial) {
                    svg.append(svgElement('line', { x1: x - 10, x2: x + 10, y1: y(eventIndex), y2: y(eventIndex), class: 'stop', stroke: color }));
                } else {
                    svg.append(svgElement('path', { d: `M ${x} ${y(eventIndex) - 8} L ${x + 6} ${y(eventIndex)} L ${x} ${y(eventIndex) + 8} L ${x - 6} ${y(eventIndex)} Z`, class: 'reattempt-stop', stroke: color }));
                }
            });
        });
        document.getElementById('timeline-map').append(svg);
    }

    loadYaml().then(() => {
        const data = window.jsyaml.load(window.COURSE_CONTENT_YAML);
        const schedule = buildSchedule(data);
        // Historical design mockups retain their comparison controls; the course home
        // has no view switch and always opens the complete semester.
        renderMap(schedule, !document.querySelector('[data-view="example"]'));
        document.querySelectorAll('[data-view]').forEach(button => {
            button.addEventListener('click', () => {
                document.querySelectorAll('[data-view]').forEach(other => other.setAttribute('aria-pressed', String(other === button)));
                renderMap(schedule, button.dataset.view === 'full');
                document.getElementById('timeline-map').scrollLeft = 0;
            });
        });
        document.getElementById('schedule-status').hidden = true;
        document.getElementById('schedule-content').hidden = false;
        document.getElementById('schedule').setAttribute('aria-busy', 'false');
        const tooltip = document.getElementById('map-tooltip');
        tooltip.addEventListener('pointerenter', () => clearTimeout(hideTimer));
        tooltip.addEventListener('pointerleave', () => {
            if (!pinnedTip && document.activeElement !== activeTip) hideTip();
        });
        document.addEventListener('keydown', event => { if (event.key === 'Escape') hideTip(); });
        document.addEventListener('pointerdown', event => {
            if (activeTip && !activeTip.contains(event.target) && !tooltip.contains(event.target)) hideTip();
        });
        document.addEventListener('scroll', () => {
            if (activeTip && document.activeElement === activeTip) showTip(activeTip, activeInfo);
            else hideTip();
        }, true);
        window.addEventListener('resize', hideTip);
    }).catch(() => {
        document.getElementById('schedule').setAttribute('aria-busy', 'false');
        const status = document.getElementById('schedule-status');
        status.textContent = 'The dated timeline could not load. Reload to try again, or check the syllabus and Canvas for dates. Reattempt A offers A; Reattempt B offers A + B; each later reattempt adds its named part.';
    });
}());
