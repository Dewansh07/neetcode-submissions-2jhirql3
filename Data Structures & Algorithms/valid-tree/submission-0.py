class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, graph, visited, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if not dfs(neighbor, graph, visited, node):
                        return False
                elif neighbor != parent:
                    return False
            return True



        if not dfs(0,graph, visited,-1):
            return False
        
        return len(visited) == n