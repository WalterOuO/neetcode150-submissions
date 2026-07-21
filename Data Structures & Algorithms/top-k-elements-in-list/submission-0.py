class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # bucket sort: Time & Space: both O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:   # Just get value, not loop, so not O(n^2)
                res.append(n)
                if len(res) == k:
                    return res
