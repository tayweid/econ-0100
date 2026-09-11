"""One-unit, displayed-price markets, independent of Manim.

Prices are inputs: this is a price-taking benchmark, not price discovery.
Participants with zero private surplus are willing to trade. Default rationing
serves the highest-value buyers and lowest-cost sellers. Values and costs are
dollars per unit; each participant can trade once in each fresh market call.
"""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Buyer:
    id: str
    value: float


@dataclass(frozen=True)
class Seller:
    id: str
    cost: float


@dataclass(frozen=True)
class Trade:
    buyer_id: str
    seller_id: str
    value: float
    cost: float
    buyer_price: float
    seller_price: float
    external_cost: float


@dataclass(frozen=True)
class MarketResult:
    trades: tuple[Trade, ...]
    willing_buyers: tuple[str, ...]
    willing_sellers: tuple[str, ...]

    @property
    def quantity(self):
        return len(self.trades)

    @property
    def consumer_surplus(self):
        return sum(t.value - t.buyer_price for t in self.trades)

    @property
    def producer_surplus(self):
        return sum(t.seller_price - t.cost for t in self.trades)

    @property
    def government_revenue(self):
        # A negative wedge represents a subsidy and negative public revenue.
        return sum(t.buyer_price - t.seller_price for t in self.trades)

    @property
    def external_damage(self):
        return sum(t.external_cost for t in self.trades)

    @property
    def total_welfare(self):
        return (self.consumer_surplus + self.producer_surplus
                + self.government_revenue - self.external_damage)


def _nonnegative(name, value):
    try:
        valid = isfinite(value) and value >= 0
    except TypeError:
        valid = False
    if not valid:
        raise ValueError(f"{name} must be a finite, nonnegative number.")


def clear_market(buyers, sellers, buyer_price, seller_price=None, *,
                 external_cost=0, buyer_priority=None,
                 price_ceiling=None, price_floor=None):
    """Match willing buyers and sellers at the supplied transaction prices.

    ``buyer_priority`` may provide a complete ordering of buyer IDs to show
    rationing. Otherwise buyers rank by value; sellers always rank by cost.
    Ties rank by ID. ``willing_*`` includes willing agents left unmatched.

    Ceiling and floor constrain buyer_price, the posted consumer price; they
    reject an illegal price rather than silently selecting another price.
    A tax is buyer_price - seller_price; its revenue is a transfer, not damage.
    External damage affects welfare, not these participants' private decisions.
    """
    buyers, sellers = tuple(buyers), tuple(sellers)
    seller_price = buyer_price if seller_price is None else seller_price
    for name, value in (("buyer_price", buyer_price),
                        ("seller_price", seller_price),
                        ("external_cost", external_cost)):
        _nonnegative(name, value)

    participants = buyers + sellers
    ids = [p.id for p in participants]
    if any(not isinstance(id_, str) or not id_ for id_ in ids):
        raise ValueError("Participant IDs must be nonempty strings.")
    if len(set(ids)) != len(ids):
        raise ValueError("Participant IDs must be unique.")
    for buyer in buyers:
        _nonnegative(f"{buyer.id} value", buyer.value)
    for seller in sellers:
        _nonnegative(f"{seller.id} cost", seller.cost)

    if price_ceiling is not None:
        _nonnegative("price_ceiling", price_ceiling)
        if buyer_price > price_ceiling:
            raise ValueError("The buyer price exceeds the price ceiling.")
    if price_floor is not None:
        _nonnegative("price_floor", price_floor)
        if buyer_price < price_floor:
            raise ValueError("The buyer price is below the price floor.")

    if buyer_priority is None:
        buyers = sorted(buyers, key=lambda b: (-b.value, b.id))
    else:
        priority = tuple(buyer_priority)
        if len(priority) != len(buyers) or set(priority) != {b.id for b in buyers}:
            raise ValueError("buyer_priority must list each buyer ID once.")
        rank = {id_: index for index, id_ in enumerate(priority)}
        buyers = sorted(buyers, key=lambda b: rank[b.id])
    sellers = sorted(sellers, key=lambda s: (s.cost, s.id))
    willing_buyers = [b for b in buyers if b.value >= buyer_price]
    willing_sellers = [s for s in sellers if s.cost <= seller_price]
    trades = tuple(
        Trade(b.id, s.id, b.value, s.cost, buyer_price, seller_price, external_cost)
        for b, s in zip(willing_buyers, willing_sellers)
    )
    return MarketResult(trades, tuple(b.id for b in willing_buyers),
                        tuple(s.id for s in willing_sellers))


def efficient_quantity(values, costs, external_cost=0):
    """Count strictly beneficial units under highest-value/lowest-cost allocation.

    A unit with zero social gain is omitted by convention. This welfare
    benchmark does not prescribe the market's price or trading process.
    """
    values, costs = tuple(values), tuple(costs)
    _nonnegative("external_cost", external_cost)
    for value in values:
        _nonnegative("value", value)
    for cost in costs:
        _nonnegative("cost", cost)
    return sum(value - cost - external_cost > 0
               for value, cost in zip(sorted(values, reverse=True), sorted(costs)))
