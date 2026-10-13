"""Posted-price mechanics for B3's episode scene (Track B, 02_Episode_Storyboard.md).

Sellers post tags; buyers are served at a tag or wait in a queue. When the
tags are wrong, incentives fix them: a queue bids tags up, crates bid them
down. Everything here is pure Python with no Manim dependency, so the scene
computes every state before anything moves (the panel is the truth; the
world is staging).

Lives beside market_model.py rather than inside it: that file is shared
with Track A and stays untouched while both tracks are in flight. Fold in
later if wanted.

Conventions. Agents are integer IDs (index into the value/cost lists) and
act in ID order; every tie breaks by ID. A market is the pair
``(tags, served)``: ``tags[s]`` is seller s's posted price or None when the
tag is pulled; ``served[b] = s`` threads buyer b to seller s at s's tag.
One unit each. Nobody deals at a loss.
"""

TICK = 0.25


def going(tags, served=None):
    """The going price: what a buyer arriving now would pay. The lowest
    crated tag while crates exist (a cheaper tag already serving someone
    is not on offer), else the lowest posted tag; None when nothing is
    posted."""
    posted = [t for t in tags.values() if t is not None]
    if served is not None:
        open_ = [tags[s] for s in crates(tags, served)]
        if open_:
            return min(open_)
    return min(posted) if posted else None


def quantities(values, costs, price):
    """(Qd, Qs) at one price: buyers with MB >= price, sellers with MC <= price."""
    if price is None:
        return 0, 0
    return (sum(v >= price for v in values), sum(c <= price for c in costs))


def crates(tags, served):
    """Posted sellers with no buyer, in ID order."""
    taken = set(served.values())
    return [s for s in sorted(tags) if tags[s] is not None and s not in taken]


def queue(values, tags, served):
    """Willing (MB >= going price) but unserved buyers, in ID order."""
    g = going(tags, served)
    if g is None:
        return []
    return [b for b in range(len(values)) if b not in served and values[b] >= g]


def post(values, costs, price, choice=None):
    """Every seller who can post at ``price`` does; then serve at posted prices."""
    tags = {s: (price if costs[s] <= price else None) for s in range(len(costs))}
    return serve(values, tags, {}, choice)


def serve(values, tags, served, choice=None):
    """Queued buyers buy from crated sellers they can afford, cheapest tag
    first (ties by ID). ``choice`` maps a buyer to a preferred seller list;
    a listed seller is taken when crated and affordable, else the default.
    Returns (tags, served) with the same tags."""
    served = dict(served)
    for b in queue(values, tags, served):
        open_ = [s for s in crates(tags, served) if tags[s] <= values[b]]
        if not open_:
            continue
        pick = next((s for s in (choice or {}).get(b, []) if s in open_), None)
        if pick is None:
            pick = min(open_, key=lambda s: (tags[s], s))
        served[b] = pick
    return tags, served


def overbid(values, tags, served, b, s, offer):
    """Buyer b offers seller s more than s's tag; s switches to b and the
    displaced buyer joins the queue. Returns (tags, served, displaced)."""
    if offer <= tags[s] or offer > values[b]:
        raise ValueError("An overbid must beat the tag and stay within MB.")
    tags, served = dict(tags), dict(served)
    displaced = next((x for x, t in served.items() if t == s), None)
    if displaced is not None:
        del served[displaced]
    served.pop(b, None)
    tags[s] = offer
    served[b] = s
    return tags, served, displaced


def undercut(values, costs, tags, served, s, new_tag):
    """Seller s cuts to ``new_tag`` (never below MC); then buyers switch to
    cheaper crated tags and willing unserved buyers step in, in ID order.
    Returns (tags, served)."""
    if new_tag >= tags[s] or new_tag < costs[s]:
        raise ValueError("A cut must lower the tag and stay at or above MC.")
    tags = dict(tags)
    tags[s] = new_tag
    return switch(values, tags, served)


def switch(values, tags, served):
    """Buyers act in ID order: a served buyer moves to a strictly cheaper
    crated tag; an unserved buyer takes the cheapest crated tag within MB."""
    served = dict(served)
    for b in range(len(values)):
        open_ = [s for s in crates(tags, served) if tags[s] <= values[b]]
        if b in served:
            open_ = [s for s in open_ if tags[s] < tags[served[b]]]
        if open_:
            served[b] = min(open_, key=lambda s: (tags[s], s))
    return tags, served


def shortage_round(values, costs, tags, served):
    """One round of a shortage: each queued buyer (ID order) overbids the
    cheapest serving seller not yet overbid this round, by a tick, if their
    MB allows. Then sellers with MC at or below the new going price post at
    it, and the queue is served. Returns (tags, served, moves) where moves
    lists (buyer, seller, displaced) for the world to stage."""
    tags, served = dict(tags), dict(served)
    moves, hit = [], set()
    for b in queue(values, tags, served):
        serving = [s for s in set(served.values()) if s not in hit
                   and tags[s] + TICK <= values[b]]
        if not serving:
            continue
        s = min(serving, key=lambda s: (tags[s], s))
        tags, served, displaced = overbid(values, tags, served, b, s, tags[s] + TICK)
        moves.append((b, s, displaced))
        hit.add(s)
    g = going(tags, served)
    for s in range(len(costs)):
        if tags[s] is None and costs[s] <= g:
            tags[s] = g
    tags, served = serve(values, tags, served)
    return tags, served, moves


def excess_round(values, costs, tags, served):
    """One round of an excess: every crated seller cuts a tick, or pulls the
    tag when a cut would go below MC; then buyers switch and step in.
    Returns (tags, served, cut, pulled)."""
    tags = dict(tags)
    cut, pulled = [], []
    for s in crates(tags, served):
        if tags[s] - TICK >= costs[s]:
            tags[s] = round(tags[s] - TICK, 2)
            cut.append(s)
        else:
            tags[s] = None
            pulled.append(s)
    tags, served = switch(values, tags, served)
    return tags, served, cut, pulled


def settled(values, costs, tags, served):
    """No crates, no queue, and no profitable overbid or undercut exists."""
    if crates(tags, served) or queue(values, tags, served):
        return False
    for b in range(len(values)):
        if b in served:
            continue
        if any(t is not None and t + TICK <= values[b] for t in tags.values()):
            return False
    return True


def run_shortage(values, costs, tags, served):
    """Rounds until the queue is empty or a round changes nothing.
    Returns the list of (tags, served, moves) after each round."""
    rounds = []
    while queue(values, tags, served):
        new_tags, new_served, moves = shortage_round(values, costs, tags, served)
        if (new_tags, new_served) == (tags, served):
            break
        tags, served = new_tags, new_served
        rounds.append((tags, served, moves))
    return rounds


def run_excess(values, costs, tags, served):
    """Rounds until no crates remain or a round changes nothing.
    Returns the list of (tags, served, cut, pulled) after each round."""
    rounds = []
    while crates(tags, served):
        new_tags, new_served, cut, pulled = excess_round(values, costs, tags, served)
        if (new_tags, new_served) == (tags, served):
            break
        tags, served = new_tags, new_served
        rounds.append((tags, served, cut, pulled))
    return rounds
