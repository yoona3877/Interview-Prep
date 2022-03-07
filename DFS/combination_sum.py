class Solution(object):

    """
    Recursion using dfs

    Cautious: duplicate!
    The input consists of unique elements.
    Each element can be used multiple times, and thus need to be careful with the same elements in different order.
    Input array is sorted
    """
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(candidates, target, [], ans)

        return ans

    def dfs(self, candidates, target, sublist, ans):
        if target < 0:
            return
        elif target == 0:
            ans.append(sublist)
        else:
            for i, item in enumerate(candidates):
                # IMPORTANT: To prevent duplicates, we don't select the previous(smaller) element than
                # the chosen element.
                self.dfs(candidates[i:], target - item, sublist + [item], ans)
        return
