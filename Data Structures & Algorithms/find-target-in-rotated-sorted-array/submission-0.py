class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        for n in range(len(nums)):
            if nums[i] < nums[n]:
                i = n
        leftout = self.binary(nums[:i+1], target)
        rightout = self.binary(nums[i+1:], target)
        if leftout != -1:
            return leftout
        elif rightout != -1:
            return rightout + i + 1
        else:
            return -1


    def binary(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) //2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1