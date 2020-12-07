# 452. 用最少数量的箭引爆气球
class Solution:
    # 100ms(79.71%), 16,4MB(98.35%)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1

        return ans
