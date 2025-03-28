class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        num_rows, num_cols = len(grid), len(grid[0])
        parents = list(range(num_rows * num_cols))
        component_sizes = [1] * (num_rows * num_cols)

        def find(parent_index):
            if parents[parent_index] != parent_index:
                parents[parent_index] = find(parents[parent_index])
            return parents[parent_index]

        def union(index_a, index_b):
            root_a, root_b = find(index_a), find(index_b)
            if root_a != root_b:
                parents[root_b] = root_a
                component_sizes[root_a] += component_sizes[root_b]

        cell_values = []
        for row in range(num_rows):
            for col in range(num_cols):
                cell_values.append((grid[row][col], row, col))
        cell_values.sort(key=lambda x: x[0])

        sorted_queries = sorted((value, index) for index, value in enumerate(queries))
        answers = [0] * len(queries)
        visited = [False] * (num_rows * num_cols)
        current_value_index = 0

        for query_value, query_index in sorted_queries:
            while current_value_index < len(cell_values) and cell_values[current_value_index][0] < query_value:
                _, row, col = cell_values[current_value_index]
                cell_index = row * num_cols + col
                visited[cell_index] = True
                for delta_row, delta_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    neighbor_row, neighbor_col = row + delta_row, col + delta_col
                    if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols and visited[neighbor_row * num_cols + neighbor_col]:
                        union(cell_index, neighbor_row * num_cols + neighbor_col)
                current_value_index += 1
            answers[query_index] = component_sizes[find(0)] if visited[0] else 0

        return answers

        
        
            
if __name__ == "__main__":
    sol = Solution()
    grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5,6,2]
    print(sol.maxPoints(grid, queries))

