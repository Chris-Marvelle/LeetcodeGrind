class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,x in enumerate(nums):
            diff = target - x
            if diff in dict:
                return (dict[diff],i)
            else:
                dict[x]=i
        return (0,0)