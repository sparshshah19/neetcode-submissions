from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return the k most frequent elemenets within the array
        #sorting algorithm (O(n log n)) 
        
        #map each element, and how much is its frequency 

        freq_map = {}
        for num in nums: 
            freq_map[num] = 1 + freq_map.get(num, 0)
        
        #1:1
        #2:2
        #3:3

        combos_arr = list(freq_map.items())
        
        combos_arr.sort(reverse=True, key = lambda x:x[1])
        
        arr = []
        counter = 0
        while counter < k: 
          
          arr.append(combos_arr[0][0])
          combos_arr.pop(0)
          counter += 1
    
        return arr
