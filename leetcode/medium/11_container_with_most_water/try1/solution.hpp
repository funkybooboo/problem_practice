#pragma once

#include <vector>

class Solution {
public:
    int maxArea(const std::vector<int>& height) {
        int left = 0;
        int right = static_cast<int>(height.size()) - 1;  // Cast height.size() to int
        int max_area = 0;

        // While the two pointers haven't crossed
        while (left < right) {
            // Calculate the current area
            int width = right - left;
            int current_area = (height[left] < height[right]) ? height[left] * width : height[right] * width;

            // Update the maximum area if needed
            if (current_area > max_area) {
                max_area = current_area;
            }

            // Move the pointer pointing to the shorter line inward
            if (height[left] < height[right]) {
                ++left;
            } else {
                --right;
            }
        }

        return max_area;
    }
};
