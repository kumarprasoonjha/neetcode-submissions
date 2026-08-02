import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Step 1: Manually build frequency map - O(N) time
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

    # Step 2: Maintain a Min-Heap of size k - O(U log k) time
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)  # Discard the least frequent element

        # Step 3: Extract the elements from the heap - O(k) time
        return [num for freq, num in heap]
        