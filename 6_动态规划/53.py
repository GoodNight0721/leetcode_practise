class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr = nums[0]

        for num in nums[1:]:
            curr = max(curr + num, num)
            max_sum = max(max_sum, curr)  
        return max_sum
