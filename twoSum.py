class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for i in range (len(nums)):
                if nums[i]+nums[i+1]==target:
                    output = [i, i+1]
                    return output
            print("Output:" , output)
