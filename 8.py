class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = ''
        string2 = ''
        string3 = ''
        sign = ''
        count = 0

        if s == '' or s == '+' or s == '-':
            return 0

        for i in range(len(s)):
            if s[i] == ' ':
                string = s[i+1:]
                count += 1
            else:
                break
        
        string = s[count:]
        
        if string == '' or string == '+' or string == '-':
            return 0
        
        if string[0] == '+':
            sign = '+'
            string = string[1:]
        elif string[0] == '-':
            sign = '-'
            string = string[1:]
        else:
            sign = ''

        if string[0] != '0':
            string2 = string
        else:
            for i in range(len(string)):
                if string[i] == '0':
                    string2 = string[i+1:]
                else:
                    break
        
        for i in range(len(string2)):
            if string2[i].isdigit():
                string3 += string2[i]
            else:
                break
        
        output = sign + string3

        if string3.isdigit():
            result = int(output)

            min_num = -(2 ** 31)
            max_num = 2 ** 31 - 1

            if result < min_num:
                return min_num
            elif result > max_num:
                return max_num
            else:
                return result
        else:
            return 0