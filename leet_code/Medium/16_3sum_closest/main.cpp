#include "solution.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

int main(const int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " target num1 num2 num3 ...\n";
        return 1;
    }

    // Parse the target
    const int target = std::stoi(argv[1]);

    // Parse the numbers into a vector
    std::vector<int> nums;
    for (int i = 2; i < argc; ++i) {
        nums.push_back(std::stoi(argv[i]));
    }

    // Instantiate Solution and compute the result
    Solution solution;
    const int result = solution.threeSumClosest(nums, target);

    // Output the result
    std::cout << "The closest sum to the target is: " << result << std::endl;

    return 0;
}
