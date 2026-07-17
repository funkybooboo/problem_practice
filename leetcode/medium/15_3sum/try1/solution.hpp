#pragma once

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> result;
        std::ranges::sort(nums);  // Sort the array

        for (int i = 0; i < nums.size(); ++i) {
            // Skip duplicates for `i` to avoid redundant triplets
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            // Early exit if nums[i] is greater than zero or no valid triplet is possible
            if (nums[i] > 0) break;

            int left = i + 1, right = static_cast<int>(nums.size()) - 1;

            while (left < right) {

                if (const int sum = nums[i] + nums[left] + nums[right]; sum == 0) {
                    result.push_back({nums[i], nums[left], nums[right]});

                    // Skip duplicates for `left` and `right` pointers immediately
                    while (left < right && nums[left] == nums[left + 1]) ++left;
                    while (left < right && nums[right] == nums[right - 1]) --right;

                    // Move both pointers inward
                    ++left;
                    --right;
                } else if (sum < 0) {
                    ++left;  // We need a larger sum, so move the left pointer
                } else {
                    --right;  // We need a smaller sum, so move the right pointer
                }
            }
        }

        return result;
    }
};
