import numpy as np
class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        edge_case_tester = nums.copy()

        for query in queries:
            l, r, x = query
            if x > nums[l] or x > nums[r]:
                x = min(nums[l], nums[r])
        
        for query in queries:
            l, r, x = query
            rester = [0] * len(nums)
            rester[l] = 1
            rester[r] = 1
            edge_case_tester = np.array(edge_case_tester) - np.array(rester ) * x 
        if any(edge_case_tester > 0):
            #print("No hay suficientes restas")
            #print(f"edge_case_tester: {edge_case_tester}")
            return -1
        #print(f"edge_case_tester: {edge_case_tester} \n nums: {nums}") 
        if len(nums) == 1:
            if nums[0] == 0:
                return 0
            for index, query in enumerate(queries):
                nums[0] -= query[2]
                if nums[0] <= 0:
                    return index + 1
            return -1
        queries_used = [False] * len(queries)
        while True:
            max_index = np.argmax(nums)
            second_max_index = np.argmax(nums[:max_index] + nums[max_index + 1:])
            empty_queries = 0     
            for index, query in enumerate(queries):
                l, r, x = query
                if x:
                    if (l == max_index and nums[r]>=nums[second_max_index]) or (r == max_index and nums[l]>=nums[second_max_index]):
                        print(f"rester query{index}: {query}")
                        query[2] -= 1
                        nums[l] -= 1
                        nums[r] -= 1
                        queries_used[index] = True
                        print(f"queries_used so far: {queries_used}, {index}")

                        break
                else:
                    empty_queries += 1
            
            if not (any(nums) != 0):
                print(nums)
                print(queries_used)
                return queries_used.count(True)

            if empty_queries == len(queries):
                return -1
        


          


if __name__ == '__main__':
    nums = [8,4]
    queries = [[0,1,5],[1,1,5],[1,1,3],[1,1,4],[0,0,3],[1,1,4],[0,1,2],[1,1,3],[1,1,1]]
    s = Solution()
    print(s.minZeroArray(nums, queries))
    pass

        