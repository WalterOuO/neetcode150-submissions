class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # brute force
        # res = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area = (j-i) * min(heights[i], heights[j])
        #         res = max(res, area)

        # Two pointer: Linear Time Solution
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
   