from collections import defaultdict 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return the k most frequent elemenets within the array
        #sorting algorithm (O(n log n)) 
        count_elements = defaultdict(int)
        ls = []
        for num in nums: 
            count_elements[num] += 1
        
        #1:1 
        #2:2
        #3:3

        count_elements_sort = dict(sorted(count_elements.items(), key=lambda item:item[1],reverse= True))
        
        for key in list(count_elements_sort.keys())[:k]: 
            ls.append(key)
        return ls

