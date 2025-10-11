from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(nums: List[int], i: int, j: int) -> None:
            nums[i], nums[j] = nums[j], nums[i]

        def partition(nums: List[int], low: int, high: int) -> int:
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] < pivot:
                    swap(nums, i, j)
                    i += 1
            swap(nums, i, high)
            return i

        def quick_sort(nums: List[int], low: int, high: int) -> None:
            if low < high:
                pivot_idx = partition(nums, low, high)
                quick_sort(nums, low, pivot_idx - 1)
                quick_sort(nums, pivot_idx + 1, high)

        quick_sort(nums, 0, len(nums) - 1)
        return nums
