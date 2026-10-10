class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            freq[n] =  freq.get(n, 0) - 1
        
        heap = [(value, key) for key, value in freq.items()]

        heapq.heapify(heap)

        result =[]
        while k> 0:
            key, v = heapq.heappop(heap)
            print (key)
            result.append(v)
            k-=1

        return result

            
