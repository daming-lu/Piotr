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
        return res

obj = Solution()
# print(obj.combine(8,2))
res = obj.combine(8,2)

teams = ['Hi5', 'Deeplay', 'Team 3', 'MesaBasket', 'Test Bench', 'CarHops', 'Old Driver', 'WhoKnows']

chosen_pairs = []
for i in range(1, 8):
    # 7 games each team
    chosen = []
    for p in res:
        if p[0] in chosen or p[1] in chosen:
            continue
        if p not in chosen_pairs:
            chosen_pairs.append(p)
            chosen.append(p[0])
            chosen.append(p[1])
        if len(chosen) == 8:
            break
    # print(chosen)
    pair = []
    for cur_p in chosen:
        # pair.append(cur_p)
        pair.append(teams[cur_p-1])
        if len(pair) == 2:
            print(pair)
            pair = []

print(len(chosen_pairs))
