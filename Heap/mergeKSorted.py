# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        arr = []
        for l in lists:
            while l:
                arr.append(l)
                l = l.next
        if len(arr) == 0:
            return None

        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        heapq.heapify(arr)
        start = heapq.heappop(arr)
        curr = start
        while len(arr) > 0:
            curr.next = heapq.heappop(arr)
            curr = curr.next
        curr.next = None
        return start


