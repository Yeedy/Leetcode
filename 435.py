# 435. 无重叠区间
class Solution:
    # 贪心算法-pro
    # 76ns(98.01%), 16.6MB(60.32%)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: x[1])

        ans = 0
        end = -float('inf')  # 结束时间
        for i in intervals:
            if i[0] >= end:
                ans += 1
                end = i[1]
        return len(intervals) - ans

    # 贪心算法
    # 104ms(34.98%), 16,6MB(46.21%)
    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     if not intervals:
    #         return 0
    #
    #     intervals.sort(key=lambda x: x[0])
    #     ans = 0
    #     pre = 0
    #     for i in range(1, len(intervals)):
    #         if intervals[pre][1] > intervals[i][0]:
    #             ans += 1
    #             if intervals[pre][1] > intervals[i][1]:
    #                 pre = i
    #         else:
    #             pre = i
    #
    #     return ans
