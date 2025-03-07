class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isPrime(num):
            if num<2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        q = []
        diff = float('inf')
        pair = [-1,-1]
        for i in range(left,right+1):
            if isPrime(i): 
                q.append(i)
            while len(q)>=2:
                if abs(q[0]-q[1])<diff:
                    pair=[q[0],q[1]]
                    diff=abs(q[0]-q[1])  
                    if diff<=2: return pair
                q.pop(0)
        return pair    


    
        