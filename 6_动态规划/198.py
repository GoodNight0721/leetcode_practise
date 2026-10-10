class Solution:
    def rob(self, nums: list[int]) -> int:
        rob = nums[0]
        norob = 0
        for money in nums[1:]:
            new_rob = norob + money
            new_norob = max(rob, norob)

            rob = new_rob
            norob = new_norob
        return max(rob, norob)