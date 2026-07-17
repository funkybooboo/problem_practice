#pragma once

#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>

class Solution {
public:
    int threeSumClosest(std::vector<int>& nums, const int target) {
        std::ranges::sort(nums); // Step 1: Sort the array
        int closestSum = std::numeric_limits<int>::max(); // Initialize closest sum to a large value
        int minDiff = std::numeric_limits<int>::max(); // Track the smallest difference

        for (size_t i = 0; i < nums.size() - 2; ++i) { // Iterate through each number
            size_t left = i + 1;
            size_t right = nums.size() - 1;

            while (left < right) {
                // Use long long for intermediate calculations to avoid overflow
                const long long currentSum = static_cast<long long>(nums[i]) + nums[left] + nums[right];
                const long long diff = std::abs(static_cast<long long>(target) - currentSum);
                // Update closest sum if the current sum is closer to the target
                if (diff < minDiff) {
                    minDiff = static_cast<int>(diff);
                    closestSum = static_cast<int>(currentSum); // Convert back to int after calculation
                }

                // Adjust pointers
                if (currentSum < target) {
                    ++left; // Move left pointer to increase the sum
                } else if (currentSum > target) {
                    --right; // Move right pointer to decrease the sum
                } else {
                    // If the sum is exactly equal to the target, return it
                    return static_cast<int>(currentSum);
                }
            }
        }

        return closestSum; // Return the closest sum found
    }
};
