/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
    let maxSum = Math.min(...nums)
    for (let len = 1; len < nums.length + 1; len++) {
        for (let start = 0; start < nums.length; start++) {
            let sum = 0;
            for (let itr = start; itr < (start + len); itr++) {
                sum += nums[itr]
            }
            if (maxSum < sum) {
                maxSum = sum
            }
        }
    }
    return maxSum
};