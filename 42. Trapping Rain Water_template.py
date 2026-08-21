# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水

# height = [0,1,0,2,1,0,1,3,2,1,2,1]

# rain = 0
# if height[0] < height[1] and height[len(height)-1] < height[len(height)-2]:
#     for i in range(1, len(height)-1):
#         for j in range(1, min(i+1, len(height)-i)):
#             if height[i] < height[i-j] and height[i] < height[i+j]:
#                 ori_height = height[i]
#                 height[i] = min(height[i-j], height[i+j])
#                 rain += (height[i] - ori_height) * (2 * j - 1)
#                 continue

# print(rain)

# a O(n2) solution
# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         rain = 0
#         for i in range(len(height)):
#             left_max = max(height[:i+1])
#             right_max = max(height[i:])

#             rain += min(left_max, right_max) - height[i]

#         return rain

# a O(n)(both space and time complexity are O(n)) solution
# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         rain = 0
#         left_max = [height[0]] * len(height)
#         right_max = [height[len(height)-1]] * len(height)
#         for i in range(1, len(height)):
#             left_max[i] = max(left_max[i-1], height[i])
#         for j in range(len(height)-2, -1, -1):
#             right_max[j] = max(right_max[j+1], height[j])
#         for k in range(len(height)):
#             rain += min(left_max[k], right_max[k]) - height[k]

#         return rain

# a time complexity O(n) and space complexity O(1) solution
class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0

        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0

        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                rain += left_max - height[left]
                left += 1
            else:
                rain += right_max - height[right]
                right -= 1
        
        return rain
