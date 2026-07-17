#include "solution.hpp"
#include <gtest/gtest.h>

// Test fixture class for the Solution class
class SolutionTest : public ::testing::Test
{
protected:
    Solution solution;
};

// Test Case 1: Example from the problem statement
TEST_F(SolutionTest, TestExample1)
{
    std::vector nums = { -1, 0, 1, 2, -1, -4 };
    const std::vector<std::vector<int>> expected = {
        {-1, -1, 2},
        {-1, 0, 1}
    };

    std::vector<std::vector<int>> result = solution.threeSum(nums);

    // Check if the result matches the expected output
    ASSERT_EQ(result.size(), expected.size());

    // Check if each triplet is in the result
    for (const auto& triplet : expected) {
        ASSERT_TRUE(std::ranges::find(result.begin(), result.end(), triplet) != result.end());
    }
}

// Test Case 2: Case with no valid triplets
TEST_F(SolutionTest, TestExample2)
{
    std::vector nums = { 0, 1, 1 };
    constexpr std::vector<std::vector<int>> expected = {};

    const std::vector<std::vector<int>> result = solution.threeSum(nums);

    ASSERT_EQ(result, expected);
}

// Test Case 3: Case where all elements are zero
TEST_F(SolutionTest, TestExample3)
{
    std::vector nums = { 0, 0, 0 };
    const std::vector<std::vector<int>> expected = {
        { 0, 0, 0 }
    };

    const std::vector<std::vector<int>> result = solution.threeSum(nums);

    ASSERT_EQ(result.size(), expected.size());
    ASSERT_EQ(result[0], expected[0]);
}

// Test Case 4: Case with no triplets (all positive numbers)
TEST_F(SolutionTest, TestAllPositive)
{
    std::vector nums = { 1, 2, 3, 4, 5 };
    constexpr std::vector<std::vector<int>> expected = {};

    const std::vector<std::vector<int>> result = solution.threeSum(nums);

    ASSERT_EQ(result, expected);
}

// Test Case 5: Case with a valid triplet and duplicates
TEST_F(SolutionTest, TestWithDuplicates)
{
    std::vector nums = { -1, 0, 1, -1, 2, 2 };
    const std::vector<std::vector<int>> expected = {
        {-1, -1, 2},
        {-1, 0, 1}
    };

    std::vector<std::vector<int>> result = solution.threeSum(nums);

    ASSERT_EQ(result.size(), expected.size());

    // Check if each triplet is in the result
    for (const auto& triplet : expected) {
        ASSERT_TRUE(std::ranges::find(result.begin(), result.end(), triplet) != result.end());
    }
}

// Test Case 6: Edge case with a large array
TEST_F(SolutionTest, TestLargeInput)
{
    std::vector nums = { -100000, -50000, 0, 50000, 100000 };
    const std::vector<std::vector<int>> expected = {
        {-100000, 0, 100000},
        {-50000, 0, 50000}
    };

    std::vector<std::vector<int>> result = solution.threeSum(nums);

    ASSERT_EQ(result.size(), expected.size());
    for (const auto& triplet : expected) {
        ASSERT_TRUE(std::ranges::find(result.begin(), result.end(), triplet) != result.end());
    }
}

// Test Case 7: Edge case with fewer than 3 elements
TEST_F(SolutionTest, TestTooFewElements)
{
    std::vector nums = { 1, 2 };
    constexpr std::vector<std::vector<int>> expected = {};

    const std::vector<std::vector<int>> result = solution.threeSum(nums);

    ASSERT_EQ(result, expected);
}

// Test Case 8: Case with all negative numbers
TEST_F(SolutionTest, TestAllNegative)
{
    std::vector nums = { -5, -4, -3, -2, -1 };
    constexpr std::vector<std::vector<int>> expected = {};

    const std::vector<std::vector<int>> result = solution.threeSum(nums);

    ASSERT_EQ(result, expected);
}

// Test Case 9: Case with valid triplets and multiple duplicates
TEST_F(SolutionTest, TestMultipleDuplicates)
{
    std::vector nums = { -1, -1, 0, 0, 1, 1, 2 };
    const std::vector<std::vector<int>> expected = {
        {-1, -1, 2},
        {-1, 0, 1}
    };

    std::vector<std::vector<int>> result = solution.threeSum(nums);

    ASSERT_EQ(result.size(), expected.size());
    for (const auto& triplet : expected) {
        ASSERT_TRUE(std::ranges::find(result.begin(), result.end(), triplet) != result.end());
    }
}

// Test Case 10: Case with all identical numbers
TEST_F(SolutionTest, TestIdenticalNumbers)
{
    std::vector nums = { 3, 3, 3, 3, 3 };
    constexpr std::vector<std::vector<int>> expected = {};

    const std::vector<std::vector<int>> result = solution.threeSum(nums);

    ASSERT_EQ(result, expected);
}

// Main function to run all the tests
int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv); // Initialize Google Test
    return RUN_ALL_TESTS();                 // Run all the tests and return the result
}
