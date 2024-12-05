#include "solution.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

int main(const int argc, char** argv) {
    // Check if there are command line arguments
    if (argc < 2) {
        std::cerr << "Please provide a list of integers as command line arguments." << std::endl;
        return 1;
    }

    // Vector to store the parsed integers
    std::vector<int> nums;

    // Parse the command line arguments into a vector of integers
    for (int i = 1; i < argc; i++) {
        try {
            int num = std::stoi(argv[i]);
            nums.push_back(num);
        }
        catch ([[maybe_unused]] const std::invalid_argument& e) {
            std::cerr << "Invalid input: " << argv[i] << " is not a valid integer." << std::endl;
            return 1;
        }
    }

    // Create an instance of the Solution class and call the threeSum function
    Solution solution;

    // Print the results
    if (std::vector<std::vector<int>> result = solution.threeSum(nums); result.empty()) {
        std::cout << "No triplets found that sum to zero." << std::endl;
    } else {
        std::cout << "Triplets that sum to zero:" << std::endl;
        for (const auto& triplet : result) {
            std::cout << "[";
            for (size_t i = 0; i < triplet.size(); ++i) {
                std::cout << triplet[i];
                if (i != triplet.size() - 1) {
                    std::cout << ", ";
                }
            }
            std::cout << "]" << std::endl;
        }
    }

    return 0;
}
