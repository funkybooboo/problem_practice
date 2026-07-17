class MedianFinder:

    def __init__(self):
        self._nums = []

    def addNum(self, num: int) -> None:
        self._nums.append(num)

    def findMedian(self) -> float:
        nums = sorted(self._nums)
        n = len(nums)
        if n == 0:
            return 0
        elif n % 2 == 0:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2
        else:
            return nums[n // 2]
