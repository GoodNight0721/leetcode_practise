class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 可以把 i 想象成一根手指，从字符串左边一直往右移动。
        i = 0
        n = len(s)

        # 第一步：跳过开头的空格。
        # 注意：只跳过开头的空格，中间遇到空格就应该停止读取。
        while i < n and s[i] == " ":
            i += 1

        # 第二步：判断正负号。
        # 默认是正数；看到负号，就把 sign 改成 -1。
        sign = 1
        if i < n and s[i] == "+":
            i += 1
        elif i < n and s[i] == "-":
            sign = -1
            i += 1

        # 第三步：从左往右读取连续的数字。
        number = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 原来的数向左移动一位，再把当前数字放到个位。
            # 例如已经读到 42，接下来读到 7：
            # 42 * 10 + 7 = 427
            number = number * 10 + digit
            i += 1

        # 把前面记录的正负号加到数字上。
        number = sign * number

        # 第四步：把结果限制在 32 位有符号整数范围内。
        min_number = -(2 ** 31)
        max_number = 2 ** 31 - 1

        if number < min_number:
            return min_number
        if number > max_number:
            return max_number

        return number


if __name__ == "__main__":
    solution = Solution()

    # 题目示例
    print(solution.myAtoi("42"))             # 42
    print(solution.myAtoi("   -042"))        # -42
    print(solution.myAtoi("1337c0d3"))       # 1337
    print(solution.myAtoi("0-1"))            # 0
    print(solution.myAtoi("words and 987"))  # 0

    # 超出范围时，返回 32 位整数的边界值。
    print(solution.myAtoi("91283472332"))    # 2147483647
