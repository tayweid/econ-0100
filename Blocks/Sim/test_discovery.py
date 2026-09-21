"""Economic checks for the random-search sequence in 03_Equilibrium.py."""

import math
import unittest

from discovery import State, improvements, simulate


MB = (6, 5, 4, 3, 7, 5, 4, 3, 2, 2)
MC = (2, 4, 3, 5, 4, 2, 6, 3, 5, 6)
ASKS = (6,) * 10


class DiscoveryTests(unittest.TestCase):
    def test_replay_is_identical_and_inputs_are_not_mutated(self):
        values, costs, asks = list(MB), list(MC), list(ASKS)
        self.assertEqual(simulate(values, costs, asks, seed=17),
                         simulate(values, costs, asks, seed=17))
        self.assertEqual((values, costs, asks), (list(MB), list(MC), list(ASKS)))

    def test_every_visit_checks_one_seller_and_each_buyer_checks_once_per_round(self):
        run = simulate(MB, MC, ASKS, seed=17)
        for round_ in run.rounds:
            visits = [e.buyer for e in round_.events if e.kind == 'check']
            self.assertEqual(sorted(visits), list(range(len(MB))))

    def test_all_snapshots_have_unique_units_and_no_loss(self):
        for seed in range(12):
            run = simulate(MB, MC, ASKS, seed=seed)
            for state in [run.initial] + [r.after for r in run.rounds]:
                occupied = [s for s in state.sellers if s is not None]
                self.assertEqual(len(occupied), len(set(occupied)))
                for b, s in enumerate(state.sellers):
                    if s is not None:
                        self.assertLessEqual(MC[s], state.asks[s])
                        self.assertLessEqual(state.asks[s], MB[b])
                self.assertTrue(all(p >= c for p, c in zip(state.asks, MC)))

    def test_each_match_improves_the_relevant_standing_deal(self):
        run = simulate(MB, MC, ASKS, seed=17)
        displacements = 0
        for round_ in run.rounds:
            asks, sellers = list(round_.before.asks), list(round_.before.sellers)
            for event in round_.events:
                if event.kind == 'match':
                    b, s = event.buyer, event.seller
                    previous = sellers[b]
                    if previous is not None:
                        self.assertLess(event.price, asks[previous])
                    if event.displaced is not None:
                        self.assertEqual(sellers[event.displaced], s)
                        self.assertAlmostEqual(event.price, asks[s] + .25)
                        sellers[event.displaced] = None
                        displacements += 1
                    self.assertLessEqual(event.price, MB[b])
                    sellers[b], asks[s] = s, event.price
                elif event.kind == 'cut':
                    self.assertNotIn(event.seller, sellers)
                    self.assertAlmostEqual(event.price, asks[event.seller] - .25)
                    asks[event.seller] = event.price
            self.assertEqual(State(tuple(asks), tuple(sellers)), round_.after)
        self.assertGreater(displacements, 0)

    def test_quiet_random_round_does_not_certify_equilibrium(self):
        run = simulate([6], [2, 9], [4, 9], seed=0, max_rounds=1)
        self.assertFalse(run.settled)
        self.assertTrue(improvements([6], [2, 9], run.final))
        self.assertNotIn(0, run.final.sellers)  # the first visit missed the affordable seller

    def test_limit_and_empty_markets_are_explicit(self):
        self.assertFalse(simulate(MB, MC, ASKS, max_rounds=0).settled)
        self.assertTrue(simulate([], [], []).settled)
        self.assertTrue(simulate([6], [], []).settled)
        run = simulate([], [2], [4])
        self.assertTrue(run.settled)
        self.assertEqual(run.final.asks, (2,))

    def test_zero_gain_match_and_stopping_audit(self):
        run = simulate([4], [4], [4])
        self.assertEqual(run.final.sellers, (0,))
        self.assertTrue(run.settled)
        self.assertFalse(improvements([4], [4], run.final))

    def test_scale_up_keeps_the_first_two_deals(self):
        asks = (6,) * 10
        initial = (0, None, None, None, 4, None, None, None, None, None)
        run = simulate(MB, MC, asks, initial_sellers=initial)
        self.assertEqual(run.initial, State(asks, initial))
        self.assertTrue(run.settled)
        with self.assertRaises(ValueError):
            simulate([6, 6], [2], [4], initial_sellers=[0, 0])
        with self.assertRaises(ValueError):
            simulate([3], [2], [4], initial_sellers=[0])

    def test_two_buyers_bid_until_the_lower_value_buyer_cannot_counter(self):
        run = simulate([6, 7], [2], [4], seed=0, initial_sellers=[0, None])
        bids = [event for round_ in run.rounds for event in round_.events
                if event.kind == 'match']
        self.assertEqual([event.price for event in bids],
                         [4.25, 4.5, 4.75, 5, 5.25, 5.5, 5.75, 6, 6.25])
        self.assertEqual([event.buyer for event in bids], [1, 0, 1, 0, 1, 0, 1, 0, 1])
        self.assertEqual(run.final, State((6.25,), (None, 0)))
        self.assertTrue(run.settled)
        self.assertGreater(run.final.asks[0] + .25, 6)
        self.assertLess(run.final.asks[0], 7)

    def test_second_seller_price_convergence_is_an_actual_switch_and_cut(self):
        run = simulate([6, 7], [2, 4], [6.25, 6], seed=4, initial_sellers=[None, 0])
        actions = [(e.kind, e.buyer, e.seller, e.price)
                   for r in run.rounds for e in r.events if e.kind != 'check']
        self.assertEqual(actions, [('match', 1, 1, 6), ('cut', None, 0, 6),
                                   ('match', 0, 0, 6)])
        self.assertEqual(run.final, State((6, 6), (0, 1)))
        self.assertTrue(run.settled)
        # Two pairs alone do not force equal prices under quarter-dollar outbids.
        other_path = simulate([6, 7], [2, 4], [6.25, 6], seed=0,
                              initial_sellers=[None, 0])
        self.assertTrue(other_path.settled)
        self.assertEqual(other_path.final.asks, (6.25, 6))

    def test_presentation_runs_reach_the_supported_four_dollar_state(self):
        fixtures = [
            (284, (6, 4.5, 6, 6, 6, 6, 6, 6, 6, 6),
             (0, 1, None, None, 4, None, None, None, None, None)),
            (473, (3.25, 4, 3, 5, 4, 3, 6, 3, 5, 6),
             (None, 2, 5, 7, 0, None, None, None, None, None)),
            (249, (5, 6, 6, 6, 6, 6, 6, 6, 6, 6),
             (0, None, None, None, 5, None, None, None, None, None)),
        ]
        for seed, asks, initial in fixtures:
            run = simulate(MB, MC, asks, seed=seed, initial_sellers=initial)
            trades = [(b, s) for b, s in enumerate(run.final.sellers) if s is not None]
            self.assertTrue(run.settled)
            self.assertEqual(len(trades), 6)
            self.assertEqual({run.final.asks[s] for b, s in trades}, {4})
            self.assertEqual(sum(MB[b] - MC[s] for b, s in trades), 13)
            self.assertFalse(improvements(MB, MC, run.final))

    def test_lookout_buyer_has_one_affordable_option_including_outbid_cost(self):
        # Gary/Molly and Amanda-Grace/Andrew remain matched at $6.
        # The new buyer's MB is $5; the new seller's MC is $4, ask $4.50.
        values, costs = [6, 5, 7], [2, 4, 4]
        state = State((6, 4.5, 6), (0, None, 2))
        offers = [ask + (.25 if s in state.sellers else 0)
                  for s, ask in enumerate(state.asks)]
        self.assertEqual(offers, [6.25, 4.5, 6.25])
        choices = [action for action in improvements(values, costs, state)
                   if action[:2] == ('visit', 1)]
        self.assertEqual(choices, [('visit', 1, 1)])
        self.assertEqual(values[1] - offers[1], .5)
        self.assertEqual(offers[1] - costs[1], .5)

    def test_rejects_invalid_inputs(self):
        for values, costs, asks, kwargs in [
            ([6], [2], [1], {}), ([6], [2], [], {}),
            ([math.nan], [2], [4], {}), ([6], [2], [4], {'step': 0}),
            ([6], [2], [4], {'max_rounds': -1}), ([6], [2], [4.1], {}),
        ]:
            with self.assertRaises(ValueError):
                simulate(values, costs, asks, **kwargs)


if __name__ == '__main__':
    unittest.main()
