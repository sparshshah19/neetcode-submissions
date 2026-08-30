class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ##brute force 
    #
    #   return_arr = []

   ##      for j in range(len(nums)):
      #          if i == j: 
      #              continue 
     #           ans *= nums[j]
      ##      return_arr.append(ans)
     #   return return_arr
    
        #so basically 
        #result product = prefix product * suffix product 
        #prefix product is product of all the elements to the right 
        #suffix product is product of all the elements to the left of i 
        #store in two seperate elements of len(nums)
        #and then multiply them going in reverse or su
        res_arr = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res_arr[i] = prefix
            prefix *= nums[i]
        
        postfix = 1 
        for i in range(len(nums) - 1, -1, -1):
            res_arr[i] *= postfix 
            postfix *= nums[i]
        return res_arr
        

