class Solution(object):
    def maximumScore(self, nums, k):
        MOD = 10**9 + 7
        
        # Precompute distinct prime factors for all possible values
        max_num = 10**5
        prime_scores = [0]*(max_num+1)
        for i in range(2, max_num+1):
            if prime_scores[i] == 0:  # i is prime
                for j in range(i, max_num+1, i):
                    prime_scores[j] += 1
        
        # Get primeScore array for nums
        scores = [prime_scores[x] for x in nums]
        n = len(nums)
        
        # Compute left limits (no element to the left has score >= scores[i])
        left_limit = [0]*n
        stack = []
        for i in range(n):
            while stack and scores[stack[-1]] >= scores[i]:
                stack.pop()
            left_limit[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
        
        # Compute right limits (no element to the right has score > scores[i])
        right_limit = [n-1]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and scores[stack[-1]] > scores[i]:
                stack.pop()
            right_limit[i] = stack[-1] - 1 if stack else n-1
            stack.append(i)
        
        # Calculate how many distinct subarrays pick each index
        counts = [(nums[i], (i - left_limit[i] + 1)*(right_limit[i] - i + 1)) for i in range(n)]
        
        # Sort by value descending
        counts.sort(key=lambda x: x[0], reverse=True)
        
        answer = 1
        k_left = k
        for value, freq in counts:
            pick = min(freq, k_left)
            if pick == 0:
                break
            # Multiply answer by value^pick
            # pow(value, pick, MOD) is efficient
            answer = (answer * pow(value, pick, MOD)) % MOD
            k_left -= pick
            if k_left == 0:
                break
        
        return answer % MOD