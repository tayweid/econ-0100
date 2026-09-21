"""Posted-price checks; run: python3 -m unittest discover -s Blocks/Sim -v.

The cast is B3's episode crowd (02_Episode_Storyboard.md): ten buyers, ten
sellers, staircases crossing at $4. IDs follow the scene's arrival order;
Gary is B0, Amanda-Grace B4, Molly S0, Andrew S4.
"""

import unittest

from posted_price import (TICK, crates, excess_round, going, overbid, post,
                          quantities, queue, run_excess, run_shortage,
                          settled, shortage_round, undercut)

MB = [6, 5, 4, 3, 6, 5, 4, 3, 2, 2]
MC = [2, 4, 3, 5, 4, 2, 6, 3, 5, 6]
GARY, AMANDA_GRACE, MOLLY, ANDREW = 0, 4, 0, 4
EXCESS_CHOICE = {GARY: [ANDREW], AMANDA_GRACE: [5]}


def no_loss(tags, served):
    return all(MC[s] <= tags[s] <= MB[b] for b, s in served.items())


class PostedPriceTests(unittest.TestCase):
    def shortage(self):
        tags, served = post(MB, MC, 3)
        tags, served, _ = overbid(MB, tags, served, AMANDA_GRACE, MOLLY, 3.25)
        return tags, served, run_shortage(MB, MC, tags, served)

    def excess(self):
        tags, served = post(MB, MC, 6, choice=EXCESS_CHOICE)
        tags, served = undercut(MB, MC, tags, served, MOLLY, 5)
        tags, served = undercut(MB, MC, tags, served, ANDREW, 5.75)
        return tags, served, run_excess(MB, MC, tags, served)

    def test_quantities_match_the_storyboard_checks(self):
        self.assertEqual(quantities(MB, MC, 3), (8, 4))
        self.assertEqual(quantities(MB, MC, 6), (2, 10))
        self.assertEqual(quantities(MB, MC, 4), (6, 6))

    def test_shortage_at_three_has_a_queue_of_four_and_ties_break_by_id(self):
        tags, served = post(MB, MC, 3)
        self.assertEqual(going(tags, served), 3)
        self.assertEqual(queue(MB, tags, served), [4, 5, 6, 7])
        self.assertEqual(crates(tags, served), [])
        self.assertEqual(served, {0: 0, 1: 2, 2: 5, 3: 7})   # lowest IDs pair first
        self.assertEqual(served[GARY], MOLLY)
        self.assertIn(AMANDA_GRACE, queue(MB, tags, served))

    def test_overbid_switches_the_seller_and_displaces_her_buyer(self):
        tags, served = post(MB, MC, 3)
        tags, served, displaced = overbid(MB, tags, served, AMANDA_GRACE, MOLLY, 3.25)
        self.assertEqual(displaced, GARY)
        self.assertEqual(served[AMANDA_GRACE], MOLLY)
        self.assertEqual(tags[MOLLY], 3.25)
        self.assertEqual(queue(MB, tags, served)[0], GARY)   # Gary rebids first
        with self.assertRaises(ValueError):
            overbid(MB, tags, served, 7, MOLLY, 3.5)          # MB 3 cannot pay 3.5
        with self.assertRaises(ValueError):
            overbid(MB, tags, served, 5, MOLLY, 3.25)         # must beat the tag

    def test_shortage_converges_into_the_band_around_four(self):
        _, _, rounds = self.shortage()
        tags, served, _ = rounds[-1]
        self.assertTrue(4 - TICK <= going(tags, served) <= 4 + TICK)
        self.assertTrue(settled(MB, MC, tags, served))
        self.assertEqual(queue(MB, tags, served), [])
        self.assertEqual(crates(tags, served), [])
        self.assertEqual(quantities(MB, MC, going(tags, served)), (6, 6))

    def test_shortage_queue_declines_monotonically_and_the_chain_terminates(self):
        tags, served, rounds = self.shortage()
        counts = [len(queue(MB, tags, served))]
        for tags, served, moves in rounds:
            self.assertTrue(moves)                             # every round does something
            counts.append(len(queue(MB, tags, served)))
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertEqual(counts[-1], 0)
        self.assertLess(len(rounds), 20)

    def test_tags_only_ratchet_up_in_a_shortage(self):
        tags, served, rounds = self.shortage()
        prev = tags
        for tags, served, _ in rounds:
            for s in tags:
                if prev[s] is not None and tags[s] is not None:
                    self.assertGreaterEqual(tags[s], prev[s])
            prev = tags

    def test_sellers_enter_as_the_line_rises(self):
        tags, served, rounds = self.shortage()
        self.assertIsNone(tags[ANDREW])                        # MC 4 stays out at $3
        self.assertIsNotNone(rounds[-1][0][ANDREW])            # and posts once tags reach 4
        self.assertIsNone(rounds[-1][0][6])                    # MC 6 never posts

    def test_no_loss_participation_throughout(self):
        tags, served, rounds = self.shortage()
        self.assertTrue(no_loss(tags, served))
        for tags, served, _ in rounds:
            self.assertTrue(no_loss(tags, served))
        tags, served, rounds = self.excess()
        self.assertTrue(no_loss(tags, served))
        for tags, served, _, _ in rounds:
            self.assertTrue(no_loss(tags, served))

    def test_excess_at_six_leaves_molly_with_crates(self):
        tags, served = post(MB, MC, 6, choice=EXCESS_CHOICE)
        self.assertEqual(served, {GARY: ANDREW, AMANDA_GRACE: 5})
        self.assertEqual(len(crates(tags, served)), 8)
        self.assertIn(MOLLY, crates(tags, served))
        self.assertEqual(queue(MB, tags, served), [])

    def test_mollys_cut_swings_gary_and_andrew_cuts_too(self):
        tags, served = post(MB, MC, 6, choice=EXCESS_CHOICE)
        tags, served = undercut(MB, MC, tags, served, MOLLY, 5)
        self.assertEqual(served[GARY], MOLLY)
        self.assertIn(ANDREW, crates(tags, served))
        tags, served = undercut(MB, MC, tags, served, ANDREW, 5.75)
        self.assertEqual(served[AMANDA_GRACE], ANDREW)         # the cheaper tag wins her too
        with self.assertRaises(ValueError):
            undercut(MB, MC, tags, served, 6, 5.75)            # MC 6 cannot cut below cost

    def test_excess_converges_into_the_band_around_four(self):
        _, _, rounds = self.excess()
        tags, served, _, _ = rounds[-1]
        self.assertTrue(4 - TICK <= going(tags, served) <= 4 + TICK)
        self.assertTrue(settled(MB, MC, tags, served))
        self.assertEqual(crates(tags, served), [])
        self.assertEqual(queue(MB, tags, served), [])

    def test_excess_crates_decline_monotonically_and_tags_only_fall(self):
        tags, served, rounds = self.excess()
        counts = [len(crates(tags, served))]
        prev = tags
        for tags, served, cut, pulled in rounds:
            self.assertTrue(cut or pulled)
            counts.append(len(crates(tags, served)))
            for s in tags:
                if prev[s] is not None and tags[s] is not None:
                    self.assertLessEqual(tags[s], prev[s])
            prev = tags
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertEqual(counts[-1], 0)

    def test_high_cost_sellers_withdraw_and_new_buyers_step_in(self):
        tags, served, rounds = self.excess()
        final_tags, final_served, _, _ = rounds[-1]
        self.assertIsNone(final_tags[6])                       # MC 6 pulled the tag
        self.assertIsNone(final_tags[9])
        self.assertIsNone(final_tags[3])                       # MC 5 pulled below 5
        self.assertEqual(sorted(final_served), [0, 1, 2, 4, 5, 6])   # MB >= 4 all buy
        pulled = [s for _, _, _, p in rounds for s in p]
        self.assertEqual(pulled[:2], [6, 9])                   # the $6 sellers go first

    def test_settled_market_refuses_a_lower_offer(self):
        _, _, rounds = self.excess()
        tags, served, _, _ = rounds[-1]
        with self.assertRaises(ValueError):
            overbid(MB, tags, served, GARY, served[GARY], 3.75)
        raised = dict(tags)
        raised[ANDREW] = 4.25
        buyer = next(b for b, s in served.items() if s == ANDREW)
        self.assertLess(MB[buyer], 4.25)                       # his buyer cannot follow
        self.assertFalse(settled(MB, MC, raised, {b: s for b, s in served.items() if s != ANDREW}))

    def test_rounds_are_deterministic(self):
        first = self.shortage()[2]
        second = self.shortage()[2]
        self.assertEqual(first, second)
        self.assertEqual(shortage_round(MB, MC, *post(MB, MC, 3)),
                         shortage_round(MB, MC, *post(MB, MC, 3)))
        self.assertEqual(excess_round(MB, MC, *post(MB, MC, 6, choice=EXCESS_CHOICE)),
                         excess_round(MB, MC, *post(MB, MC, 6, choice=EXCESS_CHOICE)))


if __name__ == "__main__":
    unittest.main()
