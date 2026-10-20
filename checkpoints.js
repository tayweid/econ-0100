/* Checkpoint guide: dates come from course-content.yaml.js, just as on the Part pages.
 * Eligibility is cumulative by session name, not checkpoint date:
 * Reattempt A offers A; Reattempt B offers A+B, even when Checkpoint B precedes Reattempt A.
 */
(function () {
    'use strict';
    const assets = 'https://tayweid.github.io/course-assets/';
    const localAssets = '../tayweid.github.io/course-assets/';
    const svgNS = 'http://www.w3.org/2000/svg';
    const colors = ['var(--mark-orange)', 'var(--mark-purple)', 'var(--mark-green)', 'var(--mark-pink)', 'var(--fg)', 'var(--white)'];

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

    function shortPlace(event) {
        if (event.kind === 'final') return 'Checkpoint F';
        return event.place.length > 17 ? 'See location below' : event.place;
    }

    function buildSchedule(data) {
        const parts = Object.entries(data.parts).map(([id, part]) => ({
            id, checkpoint: part.sections.find(section => section.checkpoint)?.checkpoint
        })).filter(part => part.checkpoint);
        const events = [];
        const pending = [];
        parts.forEach((part, index) => {
            const cp = part.checkpoint;
            const final = part.id === 'F';
            if (dates(cp.date).length) events.push({
                id: 'checkpoint-' + part.id, part: part.id, kind: final ? 'final' : 'checkpoint',
                date: cp.date, name: final ? 'Final session' : 'Checkpoint ' + part.id,
                place: final ? 'Checkpoint F + reattempt' : 'In class',
                detail: cp.when || 'In your regular class.',
                // The syllabus promises a final reattempt session for earlier parts.
                available: final ? parts.slice(0, index).map(p => p.id) : [part.id]
            });
            else pending.push('Checkpoint ' + part.id + ': date to be announced.');
            if (dates(cp.reattempt_date).length) events.push({
                id: 'reattempt-' + part.id, part: part.id, kind: 'reattempt',
                date: cp.reattempt_date, name: 'Reattempt ' + part.id,
                place: cp.reattempt || 'See Canvas',
                detail: cp.reattempt_when ? cp.reattempt_when + ' · ' + cp.reattempt : cp.reattempt || 'See Canvas for logistics.',
                available: parts.slice(0, index + 1).map(p => p.id)
            });
            else if (!final) pending.push('Reattempt ' + part.id + ': date to be announced.');
        });
        events.sort((a, b) => dates(a.date)[0].localeCompare(dates(b.date)[0]) || a.id.localeCompare(b.id));
        return { parts, events, pending };
    }

    function renderMap(schedule, full) {
        const parts = full ? schedule.parts : schedule.parts.filter(part => ['A', 'B'].includes(part.id));
        const events = full ? schedule.events : schedule.events.filter(event => ['A', 'B'].includes(event.part) && event.kind !== 'final');
        const width = full ? Math.max(1250, events.length * 114 + 110) : 830;
        const height = 148 + parts.length * 65;
        const start = 148;
        const end = width - (full ? 82 : 135);
        const x = index => events.length > 1 ? start + index * (end - start) / (events.length - 1) : start;
        const svg = svgElement('svg', {
            viewBox: `0 0 ${width} ${height}`, class: 'route-map' + (full ? ' full' : ' example'),
            role: 'img', 'aria-labelledby': 'route-title route-desc'
        });
        svg.append(svgElement('title', { id: 'route-title' }, full ? 'The full checkpoint and reattempt timeline' : 'How Parts A and B continue through reattempts'));
        svg.append(svgElement('desc', { id: 'route-desc' }, events.map(event =>
            `${event.name}, ${dateLabel(event.date)}: ${event.kind === 'final' ? 'Checkpoint F and reattempts for' : event.kind === 'checkpoint' ? 'first attempt for' : 'reattempts for'} Part${event.available.length > 1 ? 's' : ''} ${event.available.join(', ')}.`
        ).join(' ') + ' Solid paths lead to first attempts; dashed paths connect later chances. A vertical tick marks an available attempt.'));
        svg.append(svgElement('line', { x1: start - 38, y1: 102, x2: width - 30, y2: 102, class: 'axis' }));
        events.forEach((event, index) => {
            const at = x(index);
            text(svg, at, 22, dateLabel(event.date), 'event-date');
            text(svg, at, 47, event.name, 'event-name');
            // Long locations and exact times remain readable in the date list.
            text(svg, at, 69, shortPlace(event), 'event-place');
            if (event.kind === 'final') text(svg, at, 86, '+ reattempts', 'event-place');
            svg.append(svgElement('line', { x1: at, y1: 94, x2: at, y2: 110, class: 'axis' }));
            svg.append(svgElement('line', { x1: at, y1: 116, x2: at, y2: height - 20, class: 'guide-line' }));
        });
        parts.forEach((part, row) => {
            const y = 151 + row * 65;
            const color = colors[schedule.parts.findIndex(p => p.id === part.id) % colors.length];
            text(svg, 14, y + 6, 'Part ' + part.id, 'part-label', 'start');
            const first = events.findIndex(event => event.part === part.id && event.kind !== 'reattempt');
            if (first < 0) return;
            const firstX = x(first);
            svg.append(svgElement('path', { d: `M ${firstX - 36} ${y} H ${firstX}`, class: 'route', stroke: color }));
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
            [{ index: first, initial: true }, ...chances.map(chance => ({ index: chance.index, initial: false }))].forEach(stop => {
                const at = x(stop.index);
                // Remove a little connecting line around each tick for legibility.
                svg.append(svgElement('rect', { x: at - 6, y: y - 14, width: 12, height: 28, fill: 'var(--bg)' }));
                svg.append(svgElement('line', { x1: at, y1: y - 12, x2: at, y2: y + 12, class: 'stop', stroke: color }));
                text(svg, at, y + 29, stop.initial ? 'First try' : part.id, 'stop-label');
            });
        });
        const map = document.getElementById('timeline-map');
        map.replaceChildren(svg);
        if (full) map.setAttribute('aria-describedby', 'map-help');
        else map.removeAttribute('aria-describedby');
        if (!full) renderCompactMap(parts, events, svg.querySelector('desc').textContent);
        requestAnimationFrame(updateScrollHint);
        const pending = document.getElementById('pending-dates');
        pending.textContent = schedule.pending.join(' ');
        pending.hidden = !full || !schedule.pending.length;
        document.getElementById('map-takeaway').replaceChildren();
        const strong = document.createElement('strong');
        strong.textContent = full ? 'Follow your part’s row. ' : 'Reattempt B means A + B. ';
        document.getElementById('map-takeaway').append(strong, full
            ? 'A tick is a chance to try that part. At each reattempt, work on the skills you still need to pass. Undated sessions are listed below.'
            : 'Still need a Part A skill? Try it at Reattempt A, again at Reattempt B, and at later reattempts. Part B joins at Reattempt B.');
    }

    function updateScrollHint() {
        const map = document.getElementById('timeline-map');
        const overflowing = map.scrollWidth > map.clientWidth + 1;
        document.getElementById('map-help').hidden = !overflowing;
        if (overflowing) map.setAttribute('aria-describedby', 'map-help');
        else map.removeAttribute('aria-describedby');
    }

    // At phone widths, turn the A/B diagram so both routes and all four stops are
    // visible together. The desktop version preserves the horizontal timeline.
    function renderCompactMap(parts, events, description) {
        const height = 112 + events.length * 92;
        const svg = svgElement('svg', {
            viewBox: `0 0 350 ${height}`, class: 'route-map compact',
            role: 'img', 'aria-labelledby': 'compact-title compact-desc'
        });
        svg.append(svgElement('title', { id: 'compact-title' }, 'Follow Parts A and B down the timeline'));
        svg.append(svgElement('desc', { id: 'compact-desc' }, description.replace('A vertical tick', 'A horizontal tick')));
        const y = index => 83 + index * 92;
        events.forEach((event, index) => {
            text(svg, 2, y(index) - 15, dateLabel(event.date), 'event-date', 'start');
            text(svg, 2, y(index) + 7, event.name, 'event-name', 'start');
            text(svg, 2, y(index) + 28, shortPlace(event), 'event-place', 'start');
            svg.append(svgElement('line', { x1: 158, y1: y(index), x2: 330, y2: y(index), class: 'guide-line' }));
        });
        parts.forEach((part, index) => {
            const x = 215 + index * 95;
            const color = colors[index];
            text(svg, x, 23, 'Part ' + part.id, 'part-label');
            const first = events.findIndex(event => event.part === part.id && event.kind === 'checkpoint');
            if (first < 0) return;
            svg.append(svgElement('path', { d: `M ${x} ${y(first) - 27} V ${y(first)}`, class: 'route', stroke: color }));
            svg.append(svgElement('path', { d: `M ${x} ${y(first)} V ${height - 47}`, class: 'route retry', stroke: color }));
            svg.append(svgElement('path', { d: `M ${x - 5} ${height - 54} L ${x} ${height - 47} L ${x + 5} ${height - 54}`, class: 'route', stroke: color }));
            text(svg, x, height - 19, 'and later', 'end-label');
            events.forEach((event, eventIndex) => {
                const initial = eventIndex === first;
                if (!initial && !(event.kind === 'reattempt' && event.available.includes(part.id))) return;
                svg.append(svgElement('rect', { x: x - 14, y: y(eventIndex) - 6, width: 28, height: 12, fill: 'var(--bg)' }));
                svg.append(svgElement('line', { x1: x - 12, x2: x + 12, y1: y(eventIndex), y2: y(eventIndex), class: 'stop', stroke: color }));
                text(svg, x, y(eventIndex) + 26, initial ? 'First try' : part.id, 'stop-label');
            });
        });
        document.getElementById('timeline-map').append(svg);
    }

    function renderDates(schedule) {
        const list = document.getElementById('date-list');
        schedule.events.forEach(event => {
            const li = document.createElement('li');
            const date = document.createElement('time');
            date.dateTime = dates(event.date)[0];
            date.textContent = dateLabel(event.date);
            const body = document.createElement('div');
            const title = document.createElement('strong');
            title.textContent = event.name;
            const description = document.createElement('div');
            description.textContent = event.kind === 'final'
                ? 'First attempt: Part F. Reattempts: Parts ' + event.available.join(', ') + '.'
                : (event.kind === 'checkpoint' ? 'First attempt: Part ' : 'Reattempts: Part' + (event.available.length > 1 ? 's ' : ' ')) + event.available.join(', ') + '.';
            const detail = document.createElement('small');
            detail.textContent = event.detail;
            body.append(title, description, detail);
            li.append(date, body);
            list.append(li);
        });
        document.getElementById('unscheduled').textContent = schedule.pending.join(' ');
    }

    loadYaml().then(() => {
        const data = window.jsyaml.load(window.COURSE_CONTENT_YAML);
        const schedule = buildSchedule(data);
        renderMap(schedule, false);
        renderDates(schedule);
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
        if (window.ResizeObserver) new ResizeObserver(updateScrollHint).observe(document.getElementById('timeline-map'));
        else window.addEventListener('resize', updateScrollHint);
    }).catch(() => {
        document.getElementById('schedule').setAttribute('aria-busy', 'false');
        const status = document.getElementById('schedule-status');
        status.textContent = 'The dated timeline could not load. Reload to try again, or check the syllabus and Canvas for dates. Reattempt A offers A; Reattempt B offers A + B; each later reattempt adds its named part.';
    });
}());
