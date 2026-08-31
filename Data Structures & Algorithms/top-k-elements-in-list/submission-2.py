class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1

        buckets = defaultdict(list)
        for n in freqs.keys():
            buckets[freqs.get(n)].append(n)

        sortedKeys = sorted(buckets.keys(), reverse=True)

        output = []
        for key in sortedKeys:
            output += buckets[key]
            if len(output) >= k:
                return output[:k]