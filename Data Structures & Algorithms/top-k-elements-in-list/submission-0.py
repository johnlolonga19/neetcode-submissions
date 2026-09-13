from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        freq = [[] for f in range(len(nums)+1)]

        for num, ct in count.items():
            freq[ct].append(num)

        result = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result


        

                           
                
            
        