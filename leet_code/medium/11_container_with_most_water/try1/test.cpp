#include "solution.hpp"
#include <gtest/gtest.h>

// Test fixture class for the Solution class
class SolutionTest : public ::testing::Test
{
protected:
    Solution solution;
};

TEST_F(SolutionTest, TestExample1)
{
    const std::vector height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    EXPECT_EQ(solution.maxArea(height), 49);
}

TEST_F(SolutionTest, TestExample2)
{
    const std::vector height = {1, 1};
    EXPECT_EQ(solution.maxArea(height), 1);
}

TEST_F(SolutionTest, TestSingleElement)
{
    const std::vector height = {10};
    // With only one line, no container can be formed
    EXPECT_EQ(solution.maxArea(height), 0);
}

TEST_F(SolutionTest, TestEqualHeight)
{
    const std::vector height = {5, 5, 5, 5, 5};
    // The largest container will be between the first and last lines
    EXPECT_EQ(solution.maxArea(height), 20); // Height is 5, width is 4
}

TEST_F(SolutionTest, TestLargeInput)
{
    const std::vector height(100000, 1); // Large input with all heights equal to 1
    // The largest area will be between the first and last lines
    EXPECT_EQ(solution.maxArea(height), 99999); // Height is 1, width is 99999
}

TEST_F(SolutionTest, TestMaxHeightAtEnds)
{
    const std::vector height = {100, 1, 2, 3, 4, 5, 100};
    // The largest area is between the first and last lines
    EXPECT_EQ(solution.maxArea(height), 100 * 6); // Height is 1, width is 6
}

TEST_F(SolutionTest, TestVerySmallInput)
{
    const std::vector height = {1, 1};
    EXPECT_EQ(solution.maxArea(height), 1); // Only two elements
}

TEST_F(SolutionTest, TestSingleLineZeroHeight)
{
    const std::vector height = {0};
    EXPECT_EQ(solution.maxArea(height), 0); // No container can be formed
}

TEST_F(SolutionTest, TestAllZeros)
{
    const std::vector height = {0, 0, 0, 0, 0};
    EXPECT_EQ(solution.maxArea(height), 0); // No water can be held
}



// Main function to run all the tests
int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv); // Initialize Google Test
    return RUN_ALL_TESTS();                 // Run all the tests and return the result
}
