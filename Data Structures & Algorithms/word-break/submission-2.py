class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        wordSet = set(wordDict)
        dp = [[None] * (n + 1) for _ in range(n + 1)]

        def dfs(start, end):

            if start == n:
                return True

            if end > n:
                return False

            if dp[start][end] is not None:
                return dp[start][end]

            if s[start:end] in wordSet:
                if dfs(end, end + 1):
                    dp[start][end] = True
                    return True

            dp[start][end] = dfs(start, end + 1)
            return dp[start][end]

        return dfs(0, 1)