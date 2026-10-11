class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        temp =[1]*len(nums)
        post =[1]*len(nums)

        
        for n in range(1, len(nums)):
            temp[n] = temp[n-1]*nums[n-1]

            
        for n in range(len(nums) - 2, -1, -1):
            post[n] = post[n+1]*nums[n+1]


        result = []
        for i in range(len(nums)):
            result.append(post[i]*temp[i])

        return result