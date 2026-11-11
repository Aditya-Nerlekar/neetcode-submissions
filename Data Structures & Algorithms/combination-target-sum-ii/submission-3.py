class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        count = {}
        A = []

        for num in candidates:
            if num not in count:
                A.append(num)
            count[num] = count.get(num, 0) + 1

        def dfs(A, i, subset, total):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(A) or total > target:
                return

            if count[A[i]] > 0:
                subset.append(A[i])
                count[A[i]] -= 1

                dfs(A, i, subset, total + A[i])

                count[A[i]] += 1
                subset.pop()

            dfs(A, i + 1, subset, total)

        dfs(A, 0, [], 0)
        return res