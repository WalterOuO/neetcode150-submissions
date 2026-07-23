class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # 如果「左半邊」為有序陣列就可以用Binary Search
            if nums[l] <= nums[m]:
                # target in lefthand side
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # 3. 否則「右半邊」必為有序陣列
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1 