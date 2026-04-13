# Memory: 8 MB•Time: 27ms•Submitted at: 04/13/2026 15:12
# Beats 99.99% at runtime, 78.34% at memory

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Convert list into dict of occurrences
        # occurrences = Counter(nums)

        # Grab k most common values
        # k_most_common = Counter(nums).most_common(k)

        # Convert to list and return
        results = []
        for num, count in Counter(nums).most_common(k):
            results.append(num)

        return results;
            
