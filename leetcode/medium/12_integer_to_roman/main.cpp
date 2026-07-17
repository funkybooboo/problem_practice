#include "solution.hpp"

#include <iostream>
#include <string>

int main(int argc, char** argv)
{
    // Check if the correct number of arguments are passed
    if (argc != 2)
    {
        std::cerr << "Usage: " << argv[0] << " <integer>" << std::endl;
        return 1; // Exit with an error code
    }

    try
    {
        // Convert the first argument to an integer
        int num = std::stoi(argv[1]);

        // Ensure the number is within the valid range (1 <= num <= 3999)
        if (num < 1 || num > 3999)
        {
            std::cerr << "Error: Number must be between 1 and 3999." << std::endl;
            return 1;
        }

        // Create an instance of the Solution class
        Solution solution;

        // Call the intToRoman method and get the result
        std::string roman = solution.intToRoman(num);

        // Print the result
        std::cout << "The Roman numeral for " << num << " is: " << roman << std::endl;
    }
    catch (const std::invalid_argument& e)
    {
        // Handle invalid argument (non-integer input)
        std::cerr << "Error: Invalid input. Please provide a valid integer." << std::endl;
        return 1;
    }
    catch (const std::out_of_range& e)
    {
        // Handle out of range error for very large or very small numbers
        std::cerr << "Error: Number out of range." << std::endl;
        return 1;
    }

    return 0; // Return success
}
