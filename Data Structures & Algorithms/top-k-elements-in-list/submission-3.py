class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        # Method 2 : Heap (min-heap): Time O(n*logk), Space O(n)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num)) # (freq, num)存入Heap, 依前者freq排序

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]