class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort(key=lambda x: x[0])
        current_day = 0
        count = 0
        for meeting in meetings:
            start, end = meeting
            if current_day > end:
                continue
            elif current_day < start:  
                count += start - current_day - 1
                current_day = end
            elif current_day >= start:
                current_day = end
        count += days - current_day
        return count  
            
if __name__ == "__main__":
    sol = Solution()
    days = 8
    meetings = [[3,4],[4,8],[2,5],[3,8]]
    print(sol.countDays(days, meetings)) # 
