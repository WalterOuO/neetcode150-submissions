import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # No matter what, we have to store count of each num into dict
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # # Methond 1 : Bucket sort: Time & Space: both O(n)
        # ## Create a bucket, count be index, store [num] as value
        # freq = [[] for i in range(len(nums) + 1)]
        # for n, c in count.items():
        #     freq[c].append(n)
        
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:   # Just get value, not loop, so not O(n^2)
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        # Method 2 : Heap (min-heap): Time O(n*logk), Space O(n)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num)) # (freq, num)存入Heap, 依前者freq排序

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
