"""
Instructor: David Parkes
CS136 PSET6: Implementation of the Balanced Bidding Agent
Authors: Rangel Milushev and Tomislav Zabcic-Matic
"""

#!/usr/bin/env python
import sys

from gsp import GSP
from util import argmax_index

class AngelSlavBB:
    """Balanced bidding agent"""
    def __init__(self, id, value, budget):
        self.id = id
        self.value = value
        self.budget = budget

    def initial_bid(self, reserve):
        return self.value / 2


    def slot_info(self, t, history, reserve):
        """
        Compute the following for each slot, assuming that everyone else
        keeps their bids constant from the previous rounds.

        Returns list of tuples [(slot_id, min_bid, max_bid)], where
        min_bid is the bid needed to tie the other-agent bid for that slot
        in the last round.  If slot_id = 0, max_bid is 2* min_bid.
        Otherwise, it's the next highest min_bid (so bidding between min_bid
        and max_bid would result in ending up in that slot)
        """
        prev_round = history.round(t-1)
        other_bids = filter(lambda (a_id, b): a_id != self.id, prev_round.bids)

        clicks = prev_round.clicks
        def compute(s):
            (min, max) = GSP.bid_range_for_slot(s, clicks, reserve, other_bids)
            if max == None:
                max = 2 * min
            return (s, min, max)
            
        info = map(compute, range(len(clicks)))
        #sys.stdout.write("slot info: %s\n" % info) #for debugging purposes
        return info


    def expected_utils(self, t, history, reserve):
        """
        Figure out the expected utility of bidding such that we win each
        slot, assuming that everyone else keeps their bids constant from
        the previous round.

        returns a list of utilities per slot.
        """
        
        """
        ******************************
        * IMPLEMENTATION STARTS HERE *
        ******************************
        """
        # we will fill the utilities list
        utilities= list()
        # getting the history for the previous round [clicks, num_slots]
        previous_round = history.round(t-1)
        clicks = previous_round.clicks
        num_slots = len(clicks)
        
        """
        get the information for the slots using the above defined function:
            Returns list of tuples [(slot_id, min_bid, max_bid)]
        """
        slot_information = self.slot_info(t, history, reserve)

        # calculate the utility for every slot
        for i in range(num_slots):
            # get the slot payment which is the minimum bid from slot_information
            slot_payment = slot_information[i][1]

            """
            If we uncomment the code below in a population of
            BB agents we get higher utilities on average.
            """            
            #if i == num_slots-1:
            #   slot_payment = reserve            
    
            # calculate the utility
            utility = clicks[i]*(self.value - slot_payment)
            utilities.append(utility)

        # return the filled list
        return utilities

    def target_slot(self, t, history, reserve):
        """Figure out the best slot to target, assuming that everyone else
        keeps their bids constant from the previous rounds.

        Returns (slot_id, min_bid, max_bid), where min_bid is the bid needed to tie
        the other-agent bid for that slot in the last round.  If slot_id = 0,
        max_bid is min_bid * 2
        """
        i =  argmax_index(self.expected_utils(t, history, reserve))
        info = self.slot_info(t, history, reserve)
        return info[i]

    def bid(self, t, history, reserve):
        """
        The Balanced bidding strategy (BB) is the strategy 
        for a player j that, given bids b_{-j},
            - targets the slot s*_j which maximizes his utility, that is,
                s*_j = argmax_s {clicks_s (v_j - t_s(j))}.
            - chooses his bid b' for the next round so as to
                satisfy the following equation:
                    clicks_{s*_j} (v_j - t_{s*_j}(j)) = 
                    clicks_{s*_j-1}(v_j - b')
                (p_x is the price/click in slot x)
        If s*_j is the top slot, bid the value v_j
        """

        previous_round = history.round(t-1)
        clicks = previous_round.clicks
        num_clicks = len(clicks)
        (slot, min_bid, max_bid) = self.target_slot(t, history, reserve)

        """
        ******************************
        * IMPLEMENTATION STARTS HERE *
        ******************************
        """
        utility = None
        if slot == 0 or min_bid > self.value:
            bid = self.value
        else:
            utility = float(clicks[slot]*(self.value - min_bid))
            bid = self.value - utility/clicks[slot - 1]

        return bid

    def __repr__(self):
        return "%s(id=%d, value=%d)" % (
            self.__class__.__name__, self.id, self.value)


