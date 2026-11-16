class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0

        while q:
            res += 1
            for _ in range(len(q)): #this line is importantant as we want to process all the nodes present in that level before incrementing res            
                cur = q.popleft()
                for c in coins:
                    nxt = cur + c
                    if nxt == amount:
                        return res

                    if nxt > amount or seen[nxt]:
                        continue

                    if nxt <= amount:
                        seen[nxt] = True
                        q.append(nxt)

        return -1


