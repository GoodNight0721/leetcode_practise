class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 思路：让 needle 在 haystack 上从左往右移动。
        # 每移动到一个位置，就截取同样长度的一小段进行比较。

        # 如果 needle 是空字符串，按照题目的常见约定返回 0。
        if needle == "":
            return 0

        # needle 比 haystack 还长，一定不可能找到。
        if len(needle) > len(haystack):
            return -1

        # i 表示每次尝试匹配的起始下标。
        # 最后一个合法起点是：len(haystack) - len(needle)。
        # range 的右边取不到，所以这里需要再加 1。
        for i in range(len(haystack) - len(needle) + 1):
            # haystack[i:i + len(needle)]：
            # 从下标 i 开始，截取一段和 needle 一样长的字符串。
            current_string = haystack[i:i + len(needle)]

            # 找到相同的字符串后，立刻返回第一次出现的下标。
            if current_string == needle:
                return i

        # 所有可能的位置都检查过了，还是没找到。
        return -1


if __name__ == "__main__":
    solution = Solution()

    # 题目示例
    print(solution.strStr("sadbutsad", "sad"))  # 0
    print(solution.strStr("leetcode", "leeto"))  # -1

    # 再测试一个从中间找到的情况
    print(solution.strStr("hello", "ll"))  # 2
