class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute force 

      #  freq_map = {}
     #   for num in nums:
       #     freq_map[num] = 1 + freq_map.get(num, 0)

        # sort (number, freq) pairs by freq descending
       # sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

      #  ans_arr = []
        #for i in range(k):
       #     ans_arr.append(sorted_items[i][0])  # take the number, not the freq

     #   return ans_arr



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #so the way that i am thinking of approaching this question, 
        #is using the bucket sort algorithm, in a hashmap. 
        
        #so for each number, if i have seen it before, i'll increase the count
        #if i haven't i will add it to my hashmap. 
        #hashmap's have two things, their key, value, we will increase the value for a particular key


        seen_map = defaultdict(int)
        #why: because now what we can do is we have default values in our dictionaries, which we can set to 0 
        for num in nums: 
                seen_map[num] = 1 + seen_map.get(num, 0)
        
        freq = []
        for i in range(len(nums) + 1):
            freq.append([]) #max amount of openings in the number of items in nums 
            
        
        for num, count in seen_map.items():
            #because items retrievers key, value pairs in tuples
            freq[count].append(num)
            #so now what we have done is that the count is mapping to the number
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: 
                    return res
       # res = []
       # for i in range(len(freq) - 1, 0, -1):
       #     for num in freq[i]: 
        #        res.append(num)
        #        if len(res) == k: 
        #            return res
            

        
        #what we will have from the above loop is 
        #1:1 , 2:2 , 3:3



