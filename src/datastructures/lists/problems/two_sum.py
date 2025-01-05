'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''
from typing import List


class Solution:
    # First brute force
    # def two_sum(self, nums: List[int], target: int) -> List[int]:
    #     index_of_num = 0
    #     for num in nums:
    #         for num0 in nums[index_of_num+1:]:
    #             if num + num0 == target:
    #                 return [index_of_num, nums.index(num0,index_of_num+1)]
    #         index_of_num += 1
    #     return []

    # Second Optimize: O(N Log N)
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        high_pointer = len(nums)-1
        low_pointer = 0
        while low_pointer != high_pointer:
            temp_sum = sorted_nums[high_pointer] + sorted_nums[low_pointer]
            if temp_sum > target:
                high_pointer -= 1
            elif temp_sum < target:
                low_pointer += 1
            else:
                break
        high_value = sorted_nums[high_pointer]
        low_value = sorted_nums[low_pointer]
        if high_value == low_value:
            return [nums.index(low_value), nums.index(low_value, nums.index(low_value)+1)]
        return [nums.index(low_value), nums.index(high_value)]