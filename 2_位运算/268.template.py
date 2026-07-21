class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expect_sum = n * (n + 1) // 2
        
        return expect_sum - sum(nums)