using System;
using System.Linq;
using FourSum;

namespace FourSumApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Validate input
            if (args.Length < 2)
            {
                Console.WriteLine("Please provide the target and a list of numbers.");
                return;
            }

            // First argument is the target
            var target = int.Parse(args[0]);

            // Remaining arguments are the numbers
            var nums = args.Skip(1).Select(int.Parse).ToArray();

            // Create an instance of the solution
            var solution = new Solution();

            // Get the result
            var result = solution.FourSum(nums, target);

            // Print the result
            Console.WriteLine("Quadruplets that sum up to " + target + ":");
            foreach (var quad in result)
            {
                Console.WriteLine("[" + string.Join(", ", quad) + "]");
            }
        }
    }
}
