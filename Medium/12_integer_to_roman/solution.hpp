#pragma once

#include <string>
#include <vector>

class Solution
{
  public:
    std::string intToRoman(int num)
    {
        // Roman numerals map in descending order of value
        std::vector<std::tuple<int, const char*>> roman_map = {
            { 1000, "M" }, { 900, "CM" }, { 500, "D" }, { 400, "CD" }, { 100, "C" }, { 90, "XC" }, { 50, "L" }, { 40, "XL" }, { 10, "X" }, { 9, "IX" }, { 5, "V" }, { 4, "IV" }, { 1, "I" }
        };

        // Estimate the maximum length of the resulting string (max 15 characters for numbers <= 3999)
        std::string result;
        result.reserve(15); // We reserve space for the worst-case scenario

        for (const auto& [value, symbol] : roman_map)
        {
            while (num >= value)
            {
                result.append(symbol); // Append the Roman symbol
                num -= value;          // Decrease num by the corresponding value
            }
        }

        return result;
    }
};
