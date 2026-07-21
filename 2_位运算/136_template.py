class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 你的原思路是：
        # 数一数每个数字出现了几次，找到只出现一次的数字。
        #
        # 这里换一个更快的办法：用异或运算 ^ 把成对数字抵消掉。
        # 只需要记住下面两条规则：
        #
        # 1. 相同数字异或后等于 0：a ^ a = 0
        # 2. 0 和任何数字异或，还是那个数字：0 ^ a = a

        answer = 0

        # 每个数字只检查一次。
        for num in nums:
            # 出现两次的数字，最后会互相抵消成 0。
            # 唯一出现一次的数字不会被抵消，所以会留在 answer 中。
            answer = answer ^ num

        return answer


if __name__ == "__main__":
    solution = Solution()

    print(solution.singleNumber([2, 2, 1]))        # 1
    print(solution.singleNumber([4, 1, 2, 1, 2]))  # 4
    print(solution.singleNumber([1]))              # 1

    # 以 [4, 1, 2, 1, 2] 为例：
    # 4 ^ 1 ^ 2 ^ 1 ^ 2
    # 可以看成：4 ^ (1 ^ 1) ^ (2 ^ 2)
    #          = 4 ^ 0 ^ 0
    #          = 4
