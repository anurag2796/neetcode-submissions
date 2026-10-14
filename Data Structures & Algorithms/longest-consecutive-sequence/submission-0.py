class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)


        # nums = [0,3,2,5,4,6,1,1]
        # nums = [50,0,3,2,5,4,6,1,1]
        # nums = [0,3,2,5,4,6,1,1
        #           8,9,10,11,12,13,14,15,16,17]
        # nums = [2]
        # nums = []

        lenMax = 0
        

        for i in nums:
            if i-1 not in numSet:
                temp = 1
                numSet.discard(i)
                i1=i+1 
                while i1 in numSet:
                    temp += 1
                    numSet.discard(i1)
                    i1+=1
                lenMax = max(lenMax, temp)
        
        return lenMax
                    

        
