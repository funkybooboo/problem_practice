int removeElement(int* nums, int numsSize, int val) {
    int k = 0; // The number of elements that are not equal to `val`

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != val) {
            nums[k] = nums[i];  // Place the element at the correct position
            k++;  // Increment the count of valid elements
        }
    }

    return k;
}
