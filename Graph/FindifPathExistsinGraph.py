# 1971. Find if Path Exists in Graph
# DFS
# TC: O(V + E)
# SC: O(V + E)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for v,u in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if(node==destination):
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True

            return False        

        return dfs(source)           




    