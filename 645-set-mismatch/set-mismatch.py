class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
    # brute
        vals = Counter(nums)
        op = [0, 0]
        for i in range(1, len(nums) + 1):
            if i not in vals:
                op[1] = i
            elif vals[i] == 2:
                op[0] = i
        return op