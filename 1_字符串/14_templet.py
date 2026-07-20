class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 防止传入空列表（虽然题目规定 strs 至少有一个字符串）
        if not strs:
            return ""

        # 先假设第一个字符串就是最长公共前缀
        prefix = strs[0]

        # 依次用 prefix 和后面的每个字符串比较
        for word in strs[1:]:
            # 如果 word 不是以 prefix 开头，就不断删掉 prefix 的最后一个字符
            # 例如："flower" 和 "flow" 比较时
            # "flower" -> "flowe" -> "flow"
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                # prefix 为空，说明所有字符串没有公共前缀
                if prefix == "":
                    return ""

        return prefix


if __name__ == "__main__":
    solution = Solution()

    # 题目示例
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # fl
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))     # 空字符串
