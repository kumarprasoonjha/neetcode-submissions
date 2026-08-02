class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        d = {}
        unique_num = set(nums)
        for n in unique_num:
            d[n] = nums.count(n)
        toplist = sorted(d, key=d.get)
        return toplist[len(unique_num)-k:] 
        