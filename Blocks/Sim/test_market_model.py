"""Economic checks; run: python3 -m unittest discover -s Blocks/Sim -v."""

import unittest
from dataclasses import FrozenInstanceError

from market_model import Buyer, Seller, clear_market, efficient_quantity


class MarketModelTests(unittest.TestCase):
    def setUp(self):
        self.buyers = [Buyer(f"B{i}", value)
                       for i, value in enumerate([12, 10, 8, 6], 1)]
        self.sellers = [Seller(f"S{i}", cost)
                        for i, cost in enumerate([2, 4, 7, 9], 1)]

    def market(self, buyer_price, **kwargs):
        return clear_market(self.buyers, self.sellers, buyer_price, **kwargs)

    def test_competitive_benchmark(self):
        result = self.market(7.5)
        self.assertEqual(result.quantity, 3)
        self.assertEqual(result.consumer_surplus, 7.5)
        self.assertEqual(result.producer_surplus, 9.5)
        self.assertEqual(result.total_welfare, 17)
        self.assertEqual(result.willing_buyers, ("B1", "B2", "B3"))
        self.assertEqual(result.willing_sellers, ("S1", "S2", "S3"))
        self.assertEqual(len({t.buyer_id for t in result.trades}), result.quantity)
        self.assertEqual(len({t.seller_id for t in result.trades}), result.quantity)

    def test_ceiling_quantity_and_rationing_are_distinct(self):
        efficient = self.market(5, price_ceiling=5)
        rationed = self.market(5, price_ceiling=5,
                               buyer_priority=["B4", "B3", "B2", "B1"])
        self.assertEqual(efficient.quantity, 2)
        self.assertEqual(efficient.total_welfare, 16)
        self.assertEqual(len(efficient.willing_buyers), 4)
        self.assertEqual(rationed.quantity, 2)
        self.assertEqual(rationed.total_welfare, 8)
        self.assertEqual(tuple(t.buyer_id for t in rationed.trades), ("B4", "B3"))

    def test_tax_revenue_is_a_transfer(self):
        result = self.market(8.5, seller_price=5.5)
        self.assertEqual(result.quantity, 2)
        self.assertEqual(result.consumer_surplus, 5)
        self.assertEqual(result.producer_surplus, 5)
        self.assertEqual(result.government_revenue, 6)
        self.assertEqual(result.total_welfare, 16)

    def test_external_damage_remains_with_corrective_tax(self):
        untaxed = self.market(7.5, external_cost=3)
        taxed = self.market(8.5, seller_price=5.5, external_cost=3)
        self.assertEqual((untaxed.quantity, untaxed.total_welfare), (3, 8))
        self.assertEqual((taxed.quantity, taxed.total_welfare), (2, 10))
        self.assertEqual(taxed.external_damage, 6)
        self.assertEqual(taxed.government_revenue, 6)
        self.assertEqual(efficient_quantity([12, 10, 8, 6], [2, 4, 7, 9], 3), 2)

    def test_subsidy_has_negative_government_revenue(self):
        result = self.market(6, seller_price=9)
        self.assertEqual(result.quantity, 4)
        self.assertEqual(result.government_revenue, -12)
        self.assertEqual(result.total_welfare, 14)

    def test_zero_private_surplus_is_willing_but_zero_social_gain_is_omitted(self):
        result = clear_market([Buyer("B", 5)], [Seller("S", 5)], 5)
        self.assertEqual(result.quantity, 1)
        self.assertEqual(result.total_welfare, 0)
        self.assertEqual(efficient_quantity([5], [5]), 0)

    def test_empty_or_unwilling_market(self):
        self.assertEqual(clear_market([], [], 5).total_welfare, 0)
        self.assertEqual(self.market(20).quantity, 0)
        self.assertEqual(self.market(1).quantity, 0)

    def test_floor_and_illegal_prices(self):
        result = self.market(10, price_floor=10)
        self.assertEqual(result.quantity, 2)
        self.assertEqual(len(result.willing_sellers), 4)
        for kwargs in ({"price_ceiling": 7}, {"price_floor": 8}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                self.market(7.5, **kwargs)

    def test_invalid_numbers_ids_and_priorities(self):
        for invalid in (-1, float("inf"), float("nan"), "five"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.market(invalid)
            with self.assertRaises(ValueError):
                clear_market([Buyer("B", invalid)], self.sellers, 5)
            with self.assertRaises(ValueError):
                clear_market(self.buyers, [Seller("S", invalid)], 5)
            with self.assertRaises(ValueError):
                self.market(5, external_cost=invalid)
        with self.assertRaises(ValueError):
            clear_market([Buyer("X", 10)], [Seller("X", 4)], 5)
        with self.assertRaises(ValueError):
            clear_market([Buyer("", 10)], [], 5)
        for priority in (["B1"], ["B1", "B1", "B3", "B4"],
                         ["B1", "B2", "B3", "unknown"]):
            with self.subTest(priority=priority), self.assertRaises(ValueError):
                self.market(5, buyer_priority=priority)

    def test_inputs_and_recorded_trades_are_unchanged(self):
        before = (self.buyers[:], self.sellers[:])
        result = self.market(5, buyer_priority=["B4", "B3", "B2", "B1"])
        self.assertEqual((self.buyers, self.sellers), before)
        with self.assertRaises(FrozenInstanceError):
            result.trades[0].buyer_price = 0
        self.assertEqual(result, self.market(5, buyer_priority=["B4", "B3", "B2", "B1"]))


if __name__ == "__main__":
    unittest.main()
