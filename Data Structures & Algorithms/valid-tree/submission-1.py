class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()
        def bfs(node, parent):
            q = deque([(node, parent)])
            visit.add(node)

            while q:
                cur, par = q.popleft()
                visit.add(cur)

                for nei in adj[cur]:
                    if nei != par:
                        if nei not in visit:
                            q.append([nei, cur])
                        else:
                            return False

            return True

            

        return bfs(0, -1) and len(visit) == n
        
