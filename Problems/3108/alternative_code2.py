from collections import deque
class Solution(object):
    def minimumCost(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        disjoint_set_parent = list(range(n))
        disjoint_set_rank = [0]*n
        disjoint_set_values = [(1 << 17) - 1] * n

        

        for node_u, node_v, weight in edges:
            self.union_sets(disjoint_set_parent, disjoint_set_rank, node_u, node_v)

        for node_u, node_v, weight in edges:
            disjoint_set_values[self.find_parent(disjoint_set_parent, node_u)] &= weight

        result = []
        for source, target in query:
            if self.find_parent(disjoint_set_parent, source) == self.find_parent(disjoint_set_parent, target):
                result.append(disjoint_set_values[self.find_parent(disjoint_set_parent, source)])
            else:
                result.append(-1)
        return result
    
    def find_parent(self, disjoint_set_parent, node):
            if disjoint_set_parent[node] != node:
                disjoint_set_parent[node] = self.find_parent(disjoint_set_parent, disjoint_set_parent[node])
            return disjoint_set_parent[node]

    def union_sets(self,disjoint_set_parent, disjoint_set_rank, a, b):
        root_a = self.find_parent(disjoint_set_parent, a)
        root_b = self.find_parent(disjoint_set_parent, b)
        if root_a != root_b:
            if disjoint_set_rank[root_a] < disjoint_set_rank[root_b]:
                root_a, root_b = root_b, root_a
            disjoint_set_parent[root_b] = root_a
            if disjoint_set_rank[root_a] == disjoint_set_rank[root_b]:
                disjoint_set_rank[root_a] += 1
        

if __name__ == '__main__':
    n = 3
    edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
    query = [[1,2]]
    print(Solution().minimumCost(n, edges, query)) # [1, 3, 2]