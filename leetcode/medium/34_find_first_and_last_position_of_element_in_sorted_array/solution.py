from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def binary_search(nums: List[int], value: int) -> int:
            """
            Binary Search to find the index of the given value in nums
            :param value: what to look for
            :return: index of value (-1 if not found)
            """
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == value:
                    return mid
                elif nums[mid] < value:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        target_index = binary_search(nums, target)
        if target_index == -1:
            return [-1, -1]

        left = target_index
        right = target_index

        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1

        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1

        return [left, right]
