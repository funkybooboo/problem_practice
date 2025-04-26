#include "solution.hpp"
#include <gtest/gtest.h>

// Test fixture class for the Solution class
class SolutionTest : public ::testing::Test
{
protected:
    Solution solution; // Create an instance of the Solution class
};

// Test Case 1: Example from the problem statement
TEST_F(SolutionTest, TestExample1) // Use TEST_F to access the fixture's member
{
    std::vector nums = { -1, 2, 1, -4 };
    constexpr int target = 1;
    EXPECT_EQ(solution.threeSumClosest(nums, target), 2);
}

// Test Case 2: All elements are zeros
TEST_F(SolutionTest, TestAllZeros)
{
    std::vector nums = {0, 0, 0};
    constexpr int target = 1;
    EXPECT_EQ(solution.threeSumClosest(nums, target), 0);
}

// Test Case 5: Mixed positive and negative numbers
TEST_F(SolutionTest, TestMixedNumbers)
{
    std::vector nums = {-10, -5, 0, 5, 10};
    constexpr int target = 1;
    EXPECT_EQ(solution.threeSumClosest(nums, target), 0); // Closest is -5 + 0 + 5 = 0
}

// Test Case 7: Array with exactly three elements
TEST_F(SolutionTest, TestExactThreeElements)
{
    std::vector nums = {1, 2, 3};
    constexpr int target = 6;
    EXPECT_EQ(solution.threeSumClosest(nums, target), 6); // Only one sum possible
}

// Main function to run all the tests
int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv); // Initialize Google Test
    return RUN_ALL_TESTS();                 // Run all the tests and return the result
}
