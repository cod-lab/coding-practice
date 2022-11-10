# EASY

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Constraints:

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

# def twoSum(nums: List[int], target: int) -> List[int]:
def twoSum(nums, target: int):

    # d[nums[0]] = {target - nums[0]}
    # d = { nums[0]: target - nums[0] }

    # O(n^2) TC
    # for i,n in enumerate(nums):     # O(n)
    #     if n in d:                  # O(1)
    #         if d[n] in nums:        # O(n)
    #             return []

    d = { target-nums[0]: 0 }
    for i in range(1,len(nums)):
    # for i in range(len(nums)):
        if nums[i] in d:
            return [i,d[nums[i]]]
        d[target-nums[i]] = i


# print(twoSum([3,2,5,3],6))
print(twoSum([3,2,4],6))

