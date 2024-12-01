#include "solution.hpp" // Include the Solution class
#include <gtest/gtest.h>

// Test fixture class for the Solution class
class SolutionTest : public ::testing::Test
{
  protected:
    Solution solution;
};

// Test case 1: Convert 3749 to Roman numeral
TEST_F(SolutionTest, TestExample1)
{
    int num = 3749;
    std::string expected = "MMMDCCXLIX";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Test case 2: Convert 58 to Roman numeral
TEST_F(SolutionTest, TestExample2)
{
    int num = 58;
    std::string expected = "LVIII";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Test case 3: Convert 1994 to Roman numeral
TEST_F(SolutionTest, TestExample3)
{
    int num = 1994;
    std::string expected = "MCMXCIV";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Test case 4: Convert 1 to Roman numeral (edge case - smallest input)
TEST_F(SolutionTest, TestSmallestInput)
{
    int num = 1;
    std::string expected = "I";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Test case 5: Convert 3999 to Roman numeral (edge case - largest input)
TEST_F(SolutionTest, TestLargestInput)
{
    int num = 3999;
    std::string expected = "MMMCMXCIX";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Test case 6: Convert 4 to Roman numeral (edge case with subtractive notation)
TEST_F(SolutionTest, TestSubtractiveNotation1)
{
    int num = 4;
    std::string expected = "IV";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Test case 7: Convert 9 to Roman numeral (edge case with subtractive notation)
TEST_F(SolutionTest, TestSubtractiveNotation2)
{
    int num = 9;
    std::string expected = "IX";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Test case 8: Convert 40 to Roman numeral (edge case with subtractive notation)
TEST_F(SolutionTest, TestSubtractiveNotation3)
{
    int num = 40;
    std::string expected = "XL";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Test case 9: Convert 90 to Roman numeral (edge case with subtractive notation)
TEST_F(SolutionTest, TestSubtractiveNotation4)
{
    int num = 90;
    std::string expected = "XC";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Test case 10: Convert 400 to Roman numeral (edge case with subtractive notation)
TEST_F(SolutionTest, TestSubtractiveNotation5)
{
    int num = 400;
    std::string expected = "CD";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Test case 11: Convert 900 to Roman numeral (edge case with subtractive notation)
TEST_F(SolutionTest, TestSubtractiveNotation6)
{
    int num = 900;
    std::string expected = "CM";
    EXPECT_EQ(solution.intToRoman(num), expected);
}

// Main function to run all the tests
int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv); // Initialize Google Test
    return RUN_ALL_TESTS();                 // Run all the tests and return the result
}
