/* Course Logistics: example Part B skills, one row each, drawn like the
 * Skillsheet Report (Keller's standing/render.py): E V H practice dots, then
 * Checkpoint B and its outcome, makeups, and Reattempt B and its outcome, with
 * the report's status squares and to-dos. Every dot and square can be clicked to see what it changes.
 * The skills are Part B's; the practice and results are made up. Rows sharing
 * a block share its practice.
 */
(function () {
    'use strict';
    const PRACTICE = [
        { letter: 'E', name: 'Exercise' },
        { letter: 'V', name: 'Vignette' },
        { letter: 'H', name: 'Homework' }
    ];
    const CHECKPOINT = 2, REATTEMPT = 3;
    const blocks = { B1: 'Demand', B2: 'Supply', B3: 'Equilibrium', B4: 'Efficiency' };
    // done: E, V, H by the Checkpoint. madeUp: practice made up before the Reattempt.
    // first / second: the result on Checkpoint B / Reattempt B when it is unlocked.
    const rows = [
        { code: 'B1.1', name: 'Demand', done: [true, true, true], first: true, madeUp: [], second: true },
        { code: 'B1.2', name: 'Consumer Surplus', done: [true, true, true], first: false, madeUp: [], second: true },
        { code: 'B2.1', name: 'Supply', done: [true, true, false], first: true, madeUp: [], second: true },
        { code: 'B2.2', name: 'Producer Surplus', done: [true, true, false], first: false, madeUp: [], second: true },
        { code: 'B3.1', name: 'Equilibrium', done: [true, false, true], first: false, madeUp: [1], second: true },
        { code: 'B4.1', name: 'Efficiency & Total Surplus', done: [true, false, false], first: false, madeUp: [1, 2], second: true }
    ];
    const block = row => row.code.split('.')[0];
    const sameBlock = row => rows.filter(other => block(other) === block(row));
    const count = row => row.done.filter(Boolean).length;
    const missing = row => PRACTICE.map((_, index) => index).filter(index => !row.done[index]);

    // The report's status squares, in the page's colors (see the .ic rules).
    const X = '<path class="ic-x" d="M5.3 5.3l5.4 5.4M10.7 5.3l-5.4 5.4"/>';
    const SQUARE = {
        passed: '', notyet_open: '', notyet_locked: X, unlocked: '', locked: X,
        unknown: '<text x="8" y="11.6" text-anchor="middle">?</text>'
    };
    const icon = state => `<svg class="ic ic-${state}" viewBox="0 0 16 16" aria-hidden="true">` +
        `<rect x="1.3" y="1.3" width="13.4" height="13.4" rx="2.4"/>${SQUARE[state]}</svg>`;
    const dot = state => `<span class="dot${state ? ' ' + state : ''}" aria-hidden="true"></span>`;

    function element(tag, className, html) {
        const node = document.createElement(tag);
        if (className) node.className = className;
        if (html !== undefined) node.innerHTML = html;
        return node;
    }

    function cell(className, label, ...content) {
        const node = element('div', 'ex-cell ' + className);
        node.setAttribute('role', 'cell');
        if (label) node.dataset.label = label;
        node.append(...content);
        return node;
    }

    function button(className, html, label, onClick) {
        const node = element('button', className, html);
        node.type = 'button';
        node.setAttribute('aria-label', label);
        node.dataset.key = label.split(':')[0];
        node.addEventListener('click', () => {
            onClick();
            render();
            document.querySelector(`[data-key="${node.dataset.key}"]`)?.focus();
        });
        return node;
    }

    // Going into a sitting: whether the skill is unlocked, and what to do on it.
    function sitting(name, state, todo) {
        return cell('ex-sitting' + (todo === 'Leave blank' ? ' blank' : ''), name,
            element('span', 'ic-still', icon(state)), element('span', 'todo', todo));
    }

    // Coming out of it: passed or not yet. An attempted result can be flipped.
    function outcome(row, name, state, result) {
        const word = state === 'passed' ? 'passed' : 'not yet';
        const mark = result
            ? button('ic-button', icon(state), `${row.code} outcome on ${name}: ${word}. Change it.`, () => { row[result] = !row[result]; })
            : element('span', 'ic-still', icon(state));
        return cell('ex-outcome' + (state === 'passed' ? ' passed' : ''), 'Outcome', mark, element('span', 'todo', word));
    }

    function renderRow(row) {
        const line = element('div', 'ex-row');
        line.setAttribute('role', 'row');
        line.append(cell('ex-code', '', document.createTextNode(row.code)), cell('ex-name', '', document.createTextNode(row.name)));

        // Practice by the Checkpoint. A missed one is closed until the Checkpoint.
        const tri = element('span', 'tri');
        PRACTICE.forEach((practice, index) => {
            const done = row.done[index];
            tri.append(button('dot-button', dot(done ? 'done' : 'closed'),
                `${practice.name} ${block(row)} by Checkpoint B, row ${row.code}: ${done ? 'done' : 'not done'}`, () => {
                    sameBlock(row).forEach(other => {
                        other.done[index] = !done;
                        other.madeUp = other.madeUp.filter(made => made !== index);
                    });
                }));
        });
        line.append(cell('ex-practice', 'E V H', tri));

        // Checkpoint B: 2 of 3 unlock the skill; a locked skill is left blank and
        // comes out not yet. Not yet is locked for the Reattempt until all 3 are in.
        const unlockedFirst = count(row) >= CHECKPOINT;
        const passedFirst = unlockedFirst && row.first;
        const notYet = n => n >= REATTEMPT ? 'notyet_open' : 'notyet_locked';
        line.append(unlockedFirst
            ? sitting('Checkpoint B', 'unlocked', 'Attempt')
            : sitting('Checkpoint B', 'locked', 'Leave blank'));
        line.append(outcome(row, 'Checkpoint B', passedFirst ? 'passed' : notYet(count(row)), unlockedFirst ? 'first' : null));

        // Makeups, after the Checkpoint: the missed practice, made up or not.
        const owed = missing(row);
        const makeups = cell('ex-makeup', 'Makeups');
        if (passedFirst || !owed.length) {
            makeups.append(element('span', 'todo quiet', passedFirst ? '—' : 'none needed'));
        } else {
            const slots = element('span', 'tri');
            PRACTICE.forEach((practice, index) => {
                if (!owed.includes(index)) return slots.append(element('span', 'dot-slot'));
                const made = row.madeUp.includes(index);
                slots.append(button('dot-button', dot(made ? 'done' : ''),
                    `${practice.name} ${block(row)} makeup, row ${row.code}: ${made ? 'made up' : 'not made up'}`, () => {
                        sameBlock(row).forEach(other => {
                            other.madeUp = made ? other.madeUp.filter(m => m !== index) : [...other.madeUp, index];
                        });
                    }));
            });
            const left = owed.filter(index => !row.madeUp.includes(index));
            makeups.append(slots, element('span', 'todo' + (left.length ? '' : ' made'),
                left.length ? 'make up ' + left.map(index => PRACTICE[index].letter).join(', ') : 'made up'));
        }
        line.append(makeups);

        // Reattempt B: passed skills stay passed; 3 of 3 unlock the rest.
        const unlockedSecond = count(row) + row.madeUp.length >= REATTEMPT;
        if (passedFirst) {
            line.append(sitting('Reattempt B', 'passed', 'Leave blank'), outcome(row, 'Reattempt B', 'passed', null));
        } else if (unlockedSecond) {
            line.append(sitting('Reattempt B', 'unlocked', 'Attempt'),
                outcome(row, 'Reattempt B', row.second ? 'passed' : 'notyet_open', 'second'));
        } else {
            line.append(sitting('Reattempt B', 'notyet_locked', 'Leave blank'), outcome(row, 'Reattempt B', 'notyet_locked', null));
        }
        return line;
    }

    function legend() {
        const key = items => items.map(([mark, text]) => `<span class="it">${mark} ${text}</span>`).join('');
        return element('div', 'ex-legend',
            '<div class="col"><div class="h">Practice</div>' +
            `<div class="row"><span class="it">${PRACTICE.map(p => `<b>${p.letter}</b> ${p.name}`).join(' · ')}</span></div>` +
            `<div class="row">${key([[dot('done'), 'done'], [dot(''), 'not done'], [dot('closed'), 'closed until the Checkpoint']])}</div></div>` +
            '<div class="col"><div class="h">Skills</div>' +
            `<div class="row">${key([[icon('passed'), 'passed'], [icon('notyet_open'), 'not yet · unlocked'], [icon('notyet_locked'), 'not yet · locked']])}</div>` +
            `<div class="row">${key([[icon('unlocked'), 'unlocked'], [icon('locked'), 'locked']])}</div></div>`);
    }

    function render() {
        const root = document.getElementById('practice-blocks');
        if (!root) return;
        const table = element('div', 'ex-table');
        table.setAttribute('role', 'table');
        table.setAttribute('aria-label', 'Example Part B skills from practice to Reattempt B');
        const head = element('div', 'ex-row ex-head');
        head.setAttribute('role', 'row');
        const header = (className, html, label) => {
            const node = element('div', 'ex-th ' + className, html);
            node.setAttribute('role', 'columnheader');
            if (label) node.setAttribute('aria-label', label);
            return node;
        };
        head.append(header('ex-title', 'Part B <span class="on">example</span>'),
            header('ex-practice', '<span class="let">' + PRACTICE.map(p => `<span>${p.letter}</span>`).join('') + '</span>', 'Exercise, Vignette, Homework'),
            header('ex-sitting', 'Checkpoint B'), header('ex-outcome', 'Outcome'), header('ex-makeup', 'Makeups'),
            header('ex-sitting', 'Reattempt B'), header('ex-outcome', 'Outcome'));
        table.append(head);
        let current;
        rows.forEach(row => {
            if (block(row) !== current) {
                current = block(row);
                const lead = element('div', 'ex-lead', `<span>${current} | ${blocks[current]}</span><span class="line"></span>`);
                lead.setAttribute('role', 'row');
                table.append(lead);
            }
            table.append(renderRow(row));
        });
        const hint = element('p', 'ex-hint', 'Click a dot or square to change it');
        root.replaceChildren(legend(), table, hint);
    }

    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render);
    else render();
}());
