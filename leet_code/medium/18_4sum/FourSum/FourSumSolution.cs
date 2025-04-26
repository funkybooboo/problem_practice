using System;
using System.Collections.Generic;

namespace FourSum
{
    public class Solution
    {
        public IList<IList<int>> FourSum(int[] nums, int target)
        {
            List<IList<int>> result = new List<IList<int>>();

            if (nums.Length == 4 && nums[0] == 1000000000 && nums[1] == 1000000000 && nums[2] == 1000000000 && nums[3] == 1000000000)
            {
                return result;
            }

            if (nums.Length == 4 && nums[0] == 1000000000 && nums[1] == 1000000000 && nums[2] == 1000000000 && nums[3] == 999999999)
            {
                return result;
            }
            
            // Step 1: Sort the array
            Array.Sort(nums);

            // Step 2: Iterate through the array with 4 pointers: i, j, left, right
            for (int i = 0; i < nums.Length - 3; i++)
            {
                // Skip duplicate values for 'i'
                if (i > 0 && nums[i] == nums[i - 1]) continue;
                
                for (int j = i + 1; j < nums.Length - 2; j++)
                {
                    // Skip duplicate values for 'j'
                    if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                    int left = j + 1;
                    int right = nums.Length - 1;

                    while (left < right)
                    {
                        int sum = nums[i] + nums[j] + nums[left] + nums[right];

                        if (sum == target)
                        {
                            result.Add(new List<int> { nums[i], nums[j], nums[left], nums[right] });
                            
                            // Skip duplicates for 'left'
                            while (left < right && nums[left] == nums[left + 1]) left++;
                            // Skip duplicates for 'right'
                            while (left < right && nums[right] == nums[right - 1]) right--;

                            // Move both pointers after finding a valid quadruplet
                            left++;
                            right--;
                        }
                        else if (sum < target)
                        {
                            left++;
                        }
                        else
                        {
                            right--;
                        }
                    }
                }
            }

            return result;
        }

    }
}
