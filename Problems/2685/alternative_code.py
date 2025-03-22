class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        matrix = self.createMatrixConnection(n, edges)
        visited = [False] * n

        def dfs(node, component):
            for i in range(n):
                if matrix[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    component.append(i)
                    dfs(i, component)

        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                component = [i]
                dfs(i, component)
                complete = True
                for u in component:
                    for v in component:
                        if u != v and matrix[u][v] == 0:
                            complete = False
                            break
                    if not complete:
                        break
                if complete:
                    count += 1

        return count

    def createMatrixConnection(self, n, edges):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for edge in edges:
            matrix[edge[0]][edge[1]] = 1
            matrix[edge[1]][edge[0]] = 1
        for i in range(n):
            matrix[i][i] = 1
        return matrix


if __name__ == "__main__":
    sol = Solution()
    n = 3
    edges = [[1,0],[2,1]]
    print(sol.countCompleteComponents(n, edges))
            