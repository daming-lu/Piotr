class Solution(object):
    def workhorse(self, res, sol_so_far, candidates, idx, k):
        if len(sol_so_far) == k:
            res.append(sol_so_far[:])
            return
        if idx >= len(candidates):
            return
        for i in range(idx, len(candidates)):
            sol_so_far.append(candidates[i])
            self.workhorse(res, sol_so_far, candidates, i + 1, k)
            sol_so_far.pop()
        return

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        sol_so_far = []
        candidates = [i + 1 for i in range(0, n)]
        print(candidates)
        self.workhorse(res, sol_so_far, candidates, 0, k)
        print(res)

obj = Solution()
# print(obj.combine(8,2))
res = obj.combine(8,2)

for i in range(1, 8):
    # 7 games each team
    chosen = set([])
