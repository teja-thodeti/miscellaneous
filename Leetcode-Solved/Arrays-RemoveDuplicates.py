'''Use two pointers when:
You’re comparing or swapping elements.
You want to do things like shrink a window, move inward, or scan efficiently.
You don’t need extra space for decision-making.

So, we use two pointer appraoch in removing duplicates '''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]: 
                nums[k] = nums[i]     
                k += 1                
        return k



            

        