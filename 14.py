class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        # for i in range(len(first_str)):
        #     prefix = prefix + first_str[i]
        #     prefix = prefix + ' '
        # prefix = prefix[:len(prefix)-1]
        # print(prefix)
        # print(len(prefix))
        min_str = min(strs, key=len)
        success = -1
        for i in range(len(min_str)):
            current_char = strs[0][i]
            flag = False
            for j in range(1, len(strs)):
                if strs[j][i] == current_char:
                    flag = True
                else:
                    flag = False
            if flag == True:
                success += 1
            else:
                break
        return prefix + min_str[:success+1]



solution = Solution()
strs = ['flower', 'flow', 'fliwht']
solution.longestCommonPrefix(strs)

