from collections import deque
class Solution(object):
    def minimumCost(self, n, edges, query):
        graph = [[] for _ in range(n)]
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
        INF = (1<<17) - 1
        answers = []
        for s,t in query:
            dist = [INF]*n
            dist[s] = INF
            q = deque([s])
            while q:
                u = q.popleft()
                for v,w in graph[u]:
                    cost2 = dist[u] & w
                    if cost2 < dist[v]:
                        dist[v] = cost2
                        q.append(v)
            answers.append(dist[t] if dist[t] != INF else -1)
        return answers
        

if __name__ == '__main__':
    n = 3
    edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
    query = [[1,2]]
    print(Solution().minimumCost(n, edges, query)) # [1, 3, 2]