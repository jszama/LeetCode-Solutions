class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        size = len(nums)
        if size < 3:
            return res

        nums.sort()

        for i in range(size):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, size - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]