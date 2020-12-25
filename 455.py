# 455. 分发饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 64ms(77.53%), 15.9MB(9.75%)
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = count = 0

        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            i += 1
            j += 1

        return count

        # 88ms(35%), 15.8MB(11%)
        # g.sort()
        # s.sort()
        # i = 0
        #
        # while i < len(g) and s:
        #     if g[i] <= s.pop(0):
        #         i += 1
        #
        # return i
