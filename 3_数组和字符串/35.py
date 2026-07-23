class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)

        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] < target and nums[i+1] > target:
                return i+1
            i += 1