/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
    let maxSum = Math.min(...nums)
    let prefixSums = [0]
    for (let i = 0; i < nums.length; i++) {
        prefixSums.push(prefixSums[prefixSums.length - 1] + nums[i]);
    }
    for (let len = 1; len < nums.length + 1; len++) {
        for (let start = 1; start <= nums.length; start++) {
            let sum = prefixSums[start + len - 1] - prefixSums[start - 1];
            // for(let itr = start; itr<(start+len);itr++){
            //     sum += nums[itr]
            // }
            console.log(prefixSums[start + len - 1] - prefixSums[start - 1])
            if (maxSum < sum) {
                maxSum = sum
            }
        }
    }
    return maxSum
};