class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Biggest difficulty in this problem: no duplicated combination
        # How: sort -> two pointer from left and right to converge
        
        res = []
        nums.sort()     # sorting use O(nlogn) time complexity
        
        # Strategy: a + b + c = 0 (three value)

        # one loop for changing the first value
        for i, a in enumerate(nums):

            # skip the duplicate values
            if i > 0 and a == nums[i-1]:
                continue
            
            # second loop to find b , c
            l = i +1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[r], nums[l]])
                    # if satisfy, just change c, cause b will change automatically
                    l += 1
                    # checking if duplicate value or not after changing c
                    while nums[l] == nums[l-1] and l <r:
                        l += 1
        return res