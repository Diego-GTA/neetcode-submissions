class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        
        for i in nums:
            my_set.add(i)
        if len(my_set) == len(nums):
            return False
        else:
            return True