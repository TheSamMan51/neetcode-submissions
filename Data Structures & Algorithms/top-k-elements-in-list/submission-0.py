class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for v, f in cnt.items():
            buckets[f].append(v)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for v in buckets[i]:
                res.append(v)
                if len(res) == k:
                    return res
        return res