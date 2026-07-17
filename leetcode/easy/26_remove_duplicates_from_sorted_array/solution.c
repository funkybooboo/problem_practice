int removeDuplicates(int* nums, const int numsSize) {
    // If the array is empty, return 0
    if (numsSize == 0) {
        return 0;
    }

    int k = 1; // Pointer to track the position of unique elements

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[i - 1]) {
            nums[k] = nums[i];
            k++;
        }
    }

    return k;
}
