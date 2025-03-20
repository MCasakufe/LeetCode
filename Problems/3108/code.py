class Solution(object):
    def minimumCost(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]

        
        """
        edges.sort(key=lambda x: x[2])
        answers = []
        for s, t in query:
            ds = DSU(n)
            cost = (1 << 17) - 1  # 131071
            for u, v, w in edges:
                if ds.find(u) != ds.find(v):
                    ds.union(u, v)
                    cost &= w
                if ds.find(s) == ds.find(t):
                    break
            answers.append(cost if ds.find(s) == ds.find(t) else -1)
        return answers

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
    """
        returnList = []
        no_weight_edges = [edge[:2] for edge in edges]
        for q in query:
            if self.isConnected(q[0], q[1], no_weight_edges):
                returnList.append(0)
            else:
                returnList.append(-1)

    def isConnected(self, u, w, edges, visited = []):
        if u == w:
            return True
        if [u,w] in edges or [w,u] in edges:
            return True
        visited.append(u)
        for edge in edges:
            if u in edge:
                if edge[0] == u and edge[1] not in visited:
                    if self.isConnected(edge[1], w, edges, visited):
                        return True
                elif edge[1] == u and edge[0] not in visited:
                    if self.isConnected(edge[0], w, edges, visited):
                        return True
        return False
    
    def connectionValue(self, u, w, edges):

        pass
    """
        

if __name__ == '__main__':
    n = 3
    edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
    query = [[1,2]]
    print(Solution().minimumCost(n, edges, query)) # [1, 3, 2]