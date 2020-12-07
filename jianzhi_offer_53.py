# 剑指 Offer 53 - II. 0～n-1中缺失的数字
class Solution:
    # 40ms(88.96%), 14.5MB(17.69%)
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid - 1

        return l

    # 124(5.20%), 14.5(28.21%)
    # def missingNumber(self, nums: List[int]) -> int:
    #     l, r = 0, len(nums)
    #
    #     while l < r:
    #         mid = int((l + r + 1) / 2)
    #         index = 0
    #         if mid in nums:
    #             for i, num in enumerate(nums):
    #                 if num == mid:
    #                     index = i
    #
    #             if index == mid:
    #                 l = mid
    #             else:
    #                 r = mid - 1
    #         else:
    #             return mid
    #
    #     return r
