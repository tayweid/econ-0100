"""Economic checks for the random-search sequence in 03_Equilibrium.py."""

import math
import unittest

from discovery import State, improvements, simulate


MB = (6, 8, 4, 3, 7, 5, 4, 3, 2, 2)
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

    def test_initial_matches_are_preserved_and_validated(self):
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
            (296, (6.25, 4.5, 6, 6, 6.25, 6, 6, 6, 6, 6),
             (1, 0, None, None, 4, None, None, None, None, None)),
            (473, (3.25, 4, 3, 5, 4, 3, 6, 3, 5, 6),
             (None, 2, 5, 7, 0, None, None, None, None, None)),
            (361, (5, 6, 6, 6, 6, 6, 6, 6, 6, 6),
             (0, 1, None, None, 5, None, None, None, None, None)),
        ]
        for seed, asks, initial in fixtures:
            run = simulate(MB, MC, asks, seed=seed, initial_sellers=initial)
            trades = [(b, s) for b, s in enumerate(run.final.sellers) if s is not None]
            self.assertTrue(run.settled)
            self.assertEqual(len(trades), 6)
            self.assertEqual({run.final.asks[s] for b, s in trades}, {4})
            self.assertEqual(sum(MB[b] - MC[s] for b, s in trades), 16)
            self.assertFalse(improvements(MB, MC, run.final))

    def test_andrews_entry_gives_both_buyers_a_permitted_improvement(self):
        values, costs = [6, 7], [2, 4]
        initial = State((6.25, 4.25), (None, 0))
        self.assertEqual(initial.asks[1] - costs[1], .25)
        self.assertIn(('visit', 1, 1), improvements(values, costs, initial))
        switched = State(initial.asks, (None, 1))
        self.assertEqual(initial.asks[0] - switched.asks[1], 2)
        self.assertIn(('visit', 0, 1), improvements(values, costs, switched))
        countered = State((6.25, 4.5), (1, None))
        self.assertEqual(countered.asks[1] - switched.asks[1], .25)
        self.assertEqual(values[0] - countered.asks[1], 1.5)
        run = simulate(values, costs, countered.asks,
                       initial_sellers=countered.sellers, max_rounds=0)
        self.assertEqual(run.initial, countered)

    def test_two_by_two_bids_and_cuts_reach_equal_prices_with_positive_gains(self):
        values, costs = [6, 7], [2, 4]
        run = simulate(values, costs, [6.25, 4.5], seed=54, initial_sellers=[1, None])
        self.assertTrue(run.settled)
        self.assertEqual(run.final, State((5.5, 5.5), (1, 0)))
        cuts = [e for r in run.rounds for e in r.events if e.kind == 'cut']
        self.assertEqual([(e.seller, e.price) for e in cuts], [(0, 6), (0, 5.75), (0, 5.5)])
        for b, s in enumerate(run.final.sellers):
            self.assertGreater(values[b] - run.final.asks[s], 0)
            self.assertGreater(run.final.asks[s] - costs[s], 0)
        self.assertFalse(improvements(values, costs, run.final))

    def test_third_buyer_excludes_a_buyer_who_gained_in_the_two_by_two(self):
        values, costs = [6, 7, 8], [2, 4]
        run = simulate(values, costs, [5.5, 5.5], seed=6, initial_sellers=[1, 0, None])
        self.assertEqual(values[0] - run.initial.asks[1], .5)
        self.assertTrue(all(values[0] > cost for cost in costs))
        self.assertEqual(run.final, State((6.25, 6.25), (None, 1, 0)))
        self.assertTrue(all(price > values[0] for price in run.final.asks))
        self.assertFalse(improvements(values, costs, run.final))
        self.assertTrue(run.settled)

    def test_third_seller_restores_an_affordable_trade_for_gary(self):
        # The two incumbent sellers each have a buyer at $6.25.
        # Gary, MB $6, returns when the third seller enters at MC $4, price $4.50.
        values, costs = [6, 8, 7], [2, 4, 4]
        state = State((6.25, 4.5, 6.25), (None, 0, 2))
        offers = [ask + (.25 if s in state.sellers else 0)
                  for s, ask in enumerate(state.asks)]
        self.assertEqual(offers, [6.5, 4.5, 6.5])
        choices = [action for action in improvements(values, costs, state)
                   if action[:2] == ('visit', 0)]
        self.assertEqual(choices, [('visit', 0, 1)])
        self.assertLess(offers[1], offers[2])
        self.assertEqual(values[0] - offers[1], 1.5)
        self.assertEqual(offers[1] - costs[1], .5)

    def test_survey_checks_the_cheapest_current_offer_including_outbids(self):
        for seed in range(12):
            run = simulate([8, 7, 5], [2, 3, 4], [6, 4, 5],
                           initial_sellers=[0, None, None], survey=True, seed=seed)
            self.assertTrue(run.settled)
            for round_ in run.rounds:
                asks, sellers = list(round_.before.asks), list(round_.before.sellers)
                for event in round_.events:
                    if event.kind == 'check':
                        offers = [ask + (.25 if s in sellers and sellers[event.buyer] != s else 0)
                                  for s, ask in enumerate(asks)]
                        self.assertEqual(event.price, min(offers))
                        self.assertEqual(event.price, offers[event.seller])
                    elif event.kind == 'match':
                        if event.displaced is not None:
                            sellers[event.displaced] = None
                        sellers[event.buyer] = event.seller
                        asks[event.seller] = event.price
                    else:
                        asks[event.seller] = event.price
                self.assertEqual(State(tuple(asks), tuple(sellers)), round_.after)

    def test_newcomer_compares_first_even_when_no_trade_is_affordable(self):
        run = simulate([6, 2], [4], [4], initial_sellers=[0, None],
                       survey=True, first_buyer=1)
        self.assertTrue(run.settled)
        self.assertEqual(run.initial, run.final)
        self.assertEqual(len(run.rounds), 1)
        first = run.rounds[0].events[0]
        self.assertEqual((first.kind, first.buyer, first.seller, first.price), ('check', 1, 0, 4.25))
        self.assertFalse(any(e.kind == 'match' for e in run.rounds[0].events))

    def test_survey_keeps_own_reservation_when_another_offer_only_ties(self):
        run = simulate([8], [3, 4], [4, 4], initial_sellers=[0],
                       survey=True, first_buyer=0)
        self.assertEqual(run.final.sellers, (0,))
        self.assertEqual(run.rounds[0].events[0].seller, 0)
        self.assertTrue(run.settled)

    def test_growth_carries_the_active_market_forward_after_each_arrival(self):
        asks = [6.25, 4.5, 6, 6, 6.25, 6, 6, 6, 6, 6]
        sellers = [1, 0, None, None, 4, None, None, None, None, None]
        active_b, active_s = [0, 1, 4], [0, 1, 4]
        visits = 0
        for side, entrant in [(side, i) for i in [2, 3, 5, 6, 7, 8, 9] for side in ['B', 'S']]:
            (active_b if side == 'B' else active_s).append(entrant)
            active_b.sort()
            active_s.sort()
            before = State(tuple(asks[s] for s in active_s), tuple(
                None if sellers[b] is None else active_s.index(sellers[b]) for b in active_b))
            run = simulate([MB[b] for b in active_b], [MC[s] for s in active_s], before.asks,
                           initial_sellers=before.sellers, survey=True, seed=6,
                           first_buyer=active_b.index(entrant) if side == 'B' else None)
            self.assertEqual(run.initial, before)
            self.assertTrue(run.settled)
            if side == 'B':
                self.assertEqual(run.rounds[0].events[0].buyer, active_b.index(entrant))
            visits += sum(e.kind == 'match' for r in run.rounds for e in r.events)
            for s, ask in zip(active_s, run.final.asks):
                asks[s] = ask
                self.assertGreaterEqual(ask, MC[s])
            for b, s in zip(active_b, run.final.sellers):
                sellers[b] = None if s is None else active_s[s]
                if s is not None:
                    self.assertLessEqual(asks[active_s[s]], MB[b])
            matched = [s for s in sellers if s is not None]
            self.assertEqual(len(matched), len(set(matched)))
            self.assertTrue(set(matched) <= set(active_s))
        self.assertEqual(visits, 37)
        self.assertEqual(sum(s is not None for s in sellers), 6)
        self.assertEqual({asks[s] for s in sellers if s is not None}, {4})
        self.assertEqual(sum(MB[b] - MC[s] for b, s in enumerate(sellers) if s is not None), 16)
        self.assertFalse(improvements(MB, MC, State(tuple(asks), tuple(sellers))))

    def test_rejects_invalid_inputs(self):
        for values, costs, asks, kwargs in [
            ([6], [2], [1], {}), ([6], [2], [], {}),
            ([math.nan], [2], [4], {}), ([6], [2], [4], {'step': 0}),
            ([6], [2], [4], {'max_rounds': -1}), ([6], [2], [4.1], {}),
            ([6], [2], [4], {'first_buyer': 1}),
        ]:
            with self.assertRaises(ValueError):
                simulate(values, costs, asks, **kwargs)


if __name__ == '__main__':
    unittest.main()
