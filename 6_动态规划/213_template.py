class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob_line(houses):
            rob = houses[0]
            norob = 0

            for money in houses[1:]:
                new_rob = norob + money
                new_norob = max(rob, norob)

                rob = new_rob
                norob = new_norob
            return max(rob, norob)

        if len(nums) == 1:
            return nums[0]

        case_a = rob_line(nums[:-1])
        case_b = rob_line(nums[1:])

        return max(case_a, case_b)
