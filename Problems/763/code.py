class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        letter_positions = [[] for _ in range(26)]
        for i, letter in enumerate(s):
            idx = ord(letter) - ord('a')
            if len(letter_positions[idx]) < 2:
                letter_positions[idx].append(i)
            else:
                letter_positions[idx][1] = i
        letter_positions = [p for p in letter_positions if len(p) > 0]
        for p in letter_positions:
            if len(p) == 1:
                p.append(p[0])
        letter_positions.sort(key=lambda x: x[0])
        partitions = []
        current_partition_start = 0
        current_partition_end = letter_positions[0][1]
        for i in range(1, len(letter_positions)):
            if letter_positions[i][0] <= current_partition_end:
                current_partition_end = max(current_partition_end, letter_positions[i][1])
            else:
                partitions.append(current_partition_end - current_partition_start + 1)
                current_partition_start = letter_positions[i][0]
                current_partition_end = letter_positions[i][1]
        partitions.append(current_partition_end - current_partition_start + 1)
        return partitions
        

        
          
            
if __name__ == "__main__":
    sol = Solution()
    s = "qiejxqfnqceocmy"
    print(sol.partitionLabels(s))

