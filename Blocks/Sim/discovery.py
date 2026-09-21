"""B3's one-unit posted-offer search; no drawing or camera state enters the model.

A visit checks one sampled seller. Matches are provisional: a better offer can
replace an incumbent until the period ends. A complete improvement audit, not
a quiet random round, determines whether the allowed process has settled.
"""

from dataclasses import dataclass
import math
import random


@dataclass(frozen=True)
class State:
    asks: tuple[float, ...]
    sellers: tuple[int | None, ...]  # buyer index -> seller, or unmatched


@dataclass(frozen=True)
class Event:
    kind: str
    buyer: int | None
    seller: int
    price: float
    displaced: int | None = None
    previous_seller: int | None = None


@dataclass(frozen=True)
class Round:
    number: int
    before: State
    after: State
    events: tuple[Event, ...]


@dataclass(frozen=True)
class Run:
    initial: State
    rounds: tuple[Round, ...]
    final: State
    settled: bool


def improvements(values, costs, state, step=0.25):
    """All allowed improvements; this audit does not choose agents' visits."""
    owners = {s: b for b, s in enumerate(state.sellers) if s is not None}
    actions = []
    for s, ask in enumerate(state.asks):
        if s not in owners and ask > costs[s] + 1e-9:
            actions.append(('cut', None, s))
    for b, value in enumerate(values):
        current = state.sellers[b]
        for s, ask in enumerate(state.asks):
            if s == current:
                continue
            offer = ask + (step if s in owners else 0)
            if offer > value + 1e-9:
                continue
            if current is not None and offer >= state.asks[current] - 1e-9:
                continue
            actions.append(('visit', b, s))
    return tuple(actions)


def simulate(values, costs, asks, *, seed=0, step=0.25, max_rounds=300,
             initial_sellers=None):
    """Seeded visits; one-tick cuts for units unreserved at both round boundaries.

    A matched buyer switches only to a strictly cheaper accepted offer. A new
    buyer can displace an incumbent by one tick. Nonnegative gains permit a
    fresh match. Zero-change rounds continue if the full audit finds a move.
    Reaching max_rounds is explicitly different from settlement.
    """
    values, costs, asks = tuple(values), tuple(costs), tuple(asks)
    if not math.isfinite(step) or step <= 0:
        raise ValueError('The price step must be finite and positive.')
    if not isinstance(max_rounds, int) or max_rounds < 0:
        raise ValueError('max_rounds must be a nonnegative integer.')
    if len(asks) != len(costs):
        raise ValueError('Every seller needs an initial ask.')
    for value in values + costs + asks:
        if not math.isfinite(value) or value < 0:
            raise ValueError('Values, costs, and asks must be finite and nonnegative.')
        if not math.isclose(value / step, round(value / step), abs_tol=1e-9):
            raise ValueError('Prices and marginals must lie on the chosen price grid.')
    if any(ask < cost for ask, cost in zip(asks, costs)):
        raise ValueError('An ask cannot start below cost.')

    # Integer ticks prevent repeated floating-point cuts from drifting below MC.
    value_ticks = [round(v / step) for v in values]
    cost_ticks = [round(c / step) for c in costs]
    ask_ticks = [round(a / step) for a in asks]
    sellers = [None] * len(values) if initial_sellers is None else list(initial_sellers)
    if len(sellers) != len(values):
        raise ValueError('Every buyer needs an initial matching state.')
    occupied = [s for s in sellers if s is not None]
    if any(not isinstance(s, int) or s < 0 or s >= len(costs) for s in occupied):
        raise ValueError('Initial matches must identify existing sellers.')
    if len(occupied) != len(set(occupied)):
        raise ValueError('A seller cannot reserve the same unit for two buyers.')
    if any(asks[s] > values[b] for b, s in enumerate(sellers) if s is not None):
        raise ValueError('Initial matches must be affordable.')
    initial = State(asks, tuple(sellers))
    state, rounds = initial, []
    rng = random.Random(seed)

    for number in range(1, max_rounds + 1):
        if not improvements(values, costs, state, step):
            break
        before = state
        open_at_start = set(range(len(costs))) - set(sellers)
        events = []
        order = list(range(len(values)))
        rng.shuffle(order)
        for b in order:
            if not costs:
                break
            s = rng.randrange(len(costs))
            current = sellers[b]
            owners = {seller: buyer for buyer, seller in enumerate(sellers)
                      if seller is not None}
            offer = ask_ticks[s] + int(s in owners and owners[s] != b)
            events.append(Event('check', b, s, offer * step))
            if s == current or offer > value_ticks[b]:
                continue
            if current is not None and offer >= ask_ticks[current]:
                continue
            displaced = owners.get(s)
            if displaced is not None:
                sellers[displaced] = None
            sellers[b] = s
            ask_ticks[s] = offer
            events.append(Event('match', b, s, offer * step, displaced, current))

        still_open = open_at_start - set(sellers)
        for s in sorted(still_open):
            if ask_ticks[s] > cost_ticks[s]:
                ask_ticks[s] = max(cost_ticks[s], ask_ticks[s] - 1)
                events.append(Event('cut', None, s, ask_ticks[s] * step))
        state = State(tuple(p * step for p in ask_ticks), tuple(sellers))
        rounds.append(Round(number, before, state, tuple(events)))

    return Run(initial, tuple(rounds), state,
               not improvements(values, costs, state, step))
