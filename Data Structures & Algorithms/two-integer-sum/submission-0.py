class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for i in range(len(nums)):
            if nums[i] in compliment.keys():
                i1 = compliment[nums[i]]
                return [i1, i]
            compliment[target - nums[i]] = i
