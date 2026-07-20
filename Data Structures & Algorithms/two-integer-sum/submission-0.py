class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # UMPIRE
        # Match: array + minus
        # Plan: store index, value in hashmap, use minus to find index
        # Implement:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            key = target - nums[i]
            if key in hashmap and hashmap[key] != i:
                return [i, hashmap[key]]
        # Review:

        # Evaluation:
        ## Time: 2 loop * n times * 1 (write and find hashmap) -> O(n)
        ## Space: one hashmap -> O(n)