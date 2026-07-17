using System;
using System.Collections.Generic;
using Xunit;
using FourSum;

namespace FourSumTests
{
    public class FourSumSolutionTests
    {
        [Fact]
        public void FourSum_Test1()
        {
            var solution = new Solution();
            var result = solution.FourSum(new[] { 1, 0, -1, 0, -2, 2 }, 0);
            var expected = new List<IList<int>>()
            {
                new List<int> { -2, -1, 1, 2 },
                new List<int> { -2, 0, 0, 2 },
                new List<int> { -1, 0, 0, 1 }
            };

            Assert.Equal(expected, result);
        }

        [Fact]
        public void FourSum_Test2()
        {
            var solution = new Solution();
            var result = solution.FourSum(new[] { 2, 2, 2, 2, 2 }, 8);
            var expected = new List<IList<int>>()
            {
                new List<int> { 2, 2, 2, 2 }
            };

            Assert.Equal(expected, result);
        }

        [Fact]
        public void FourSum_NoQuadruplet()
        {
            var solution = new Solution();
            var result = solution.FourSum(new[] { 1, 2, 3, 4 }, 100);
            var expected = new List<IList<int>>();

            Assert.Equal(expected, result);
        }
    }
}

