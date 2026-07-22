import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # Methond 1 : Bucket sort: Time & Space: both O(n)
        ## Create a bucket, count be index, store [num] as value
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:   # Just get value, not loop, so not O(n^2)
                res.append(n)
                if len(res) == k:
                    return res


