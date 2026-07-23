class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # k表示目前已经找到多少个不同的数字
        # 同时也是下一个不同数字应该写入的位置
        k = 1

        for i in range(1, len(nums)):
            # 当前数字与上一个保留下来的数字不同
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k