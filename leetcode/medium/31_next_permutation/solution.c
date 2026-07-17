void nextPermutation(int* nums, const int numsSize) {
    int i = numsSize - 2;
    // Find the first decreasing element
    while (i >= 0 && nums[i] >= nums[i + 1]) {
        i--;
    }

    if (i >= 0) {
        // Find the smallest element larger than nums[i] to the right
        int j = numsSize - 1;
        while (nums[j] <= nums[i]) {
            j--;
        }
        // Swap nums[i] and nums[j]
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    // Reverse the elements to the right of index i
    int left = i + 1;
    int right = numsSize - 1;
    while (left < right) {
        const int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
        left++;
        right--;
    }
}
