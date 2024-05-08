class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums): # set(nums) will return unique elements of nums
            return True
        return False
