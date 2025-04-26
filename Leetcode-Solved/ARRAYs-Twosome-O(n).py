#Twosome
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

#Note:local compiler asks for the missing input code.This can work in Leetcode since input is provided through leetcode ADT/interface 
