class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


print(Solution().containsDuplicate([1, 2, 3, 1]))
print(Solution().containsDuplicate([1, 2, 3]))
        