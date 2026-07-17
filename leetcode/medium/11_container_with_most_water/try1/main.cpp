#include "solution.hpp"
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

int main(const int argc, char** argv) {
    // Check if the correct number of arguments is provided
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <height1> <height2> ... <heightN>" << std::endl;
        return 1;
    }

    // Create a vector to store the heights
    std::vector<int> height;

    // Parse the command line arguments into the height vector
    for (int i = 1; i < argc; i++) {
        try {
            height.push_back(std::stoi(argv[i])); // Convert argument to int and add to vector
        } catch (const std::invalid_argument&) {
            std::cerr << "Invalid input: " << argv[i] << " is not a valid integer." << std::endl;
            return 1;
        } catch (const std::out_of_range&) {
            std::cerr << "Invalid input: " << argv[i] << " is out of range for an integer." << std::endl;
            return 1;
        }
    }

    // Create the Solution object
    Solution solution;

    // Call the maxArea function and output the result
    const int result = solution.maxArea(height);
    std::cout << "The maximum area of water the container can hold is: " << result << std::endl;

    return 0;
}
