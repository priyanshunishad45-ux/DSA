class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash_map = {}

        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 0
            
            hash_map[nums[i]] += 1

            if hash_map[nums[i]] > len(nums) // 2:
                return nums[i]