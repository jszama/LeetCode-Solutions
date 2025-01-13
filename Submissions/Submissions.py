class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in needed.keys():
                return [i, needed[nums[i]]]
            needed[target-nums[i]] = i
