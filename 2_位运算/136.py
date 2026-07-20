class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            num = nums[i]
            count = 0
            for j in range(len(nums)):
                if nums[j] == num:
                    count += 1
            if count == 1:
                return num
