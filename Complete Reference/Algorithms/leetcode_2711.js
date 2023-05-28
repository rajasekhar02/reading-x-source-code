/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var differenceOfDistinctValues = function (grid) {
    let ans = new Array(grid.length).fill(0).map(() => {
        return new Array(grid[0].length).fill(0);
    })

    let m = grid.length;
    let n = grid[0].length;
    let commonFunc = function (row, col) {
        let countDistinctInTopLeft = new Set();
        for (let tlIR = row, tlIC = col; tlIR < m && tlIC < n; tlIR++, tlIC++) {
            ans[tlIR][tlIC] = countDistinctInTopLeft.size
            countDistinctInTopLeft.add(grid[tlIR][tlIC]);
        }
        let countDistinctInBottomRight = new Set();
        /** this logic i am not able to generalize for both rows and cols */
        let tlIR = 0
        let tlIC = 0
        if (m > n) {
            /**
             * m=4, n=3
             *        col
             *      0 1 2
             *    0 x y y 
             *row 1 x x y
             *    2 o x x
             *    3 o o x
             */
            // works on o region
            if (row >= (m - n + 1)) {
                tlIR = m - 1
                tlIC = m - row - 1
            } else {
                // detects the y region
                if (col >= 1) {
                    tlIR = n - col - 1
                    tlIC = n - 1
                } else {
                    // works on x region
                    tlIR = n + row - 1
                    tlIC = n - 1
                }
            }
        } else if (m < n) {
            /**         col
             *      0 1 2 3
             *    0 x x y y
             *row 1 o x x y
             *    2 o o x x
             */
            // works on y region
            if (col >= (n - m + 1)) {
                tlIR = n - col - 1
                tlIC = n - 1
            } else {
                // works on o region
                if (col >= 1) {
                    tlIR = m - 1
                    tlIC = m + col - 1
                } else {
                    // works on x region
                    tlIR = m - 1
                    tlIC = m - row - 1
                }
            }
        } else {
            tlIR = m - col - 1
            tlIC = n - row - 1
        }
        for (;
            tlIR >= 0 && tlIC >= 0;
            tlIR--, tlIC--) {
            ans[tlIR][tlIC] = Math.abs(ans[tlIR][tlIC] - countDistinctInBottomRight.size)
            countDistinctInBottomRight.add(grid[tlIR][tlIC]);
        }
    }
    for (let row = 0; row < m; row++) {
        let col = 0
        commonFunc(row, col)
    }
    for (let col = 1; col < n; col++) {
        let row = 0
        commonFunc(row, col)
    }
    return ans;
};


[
    // [[1, 2, 3], [3, 1, 5], [3, 2, 1]],
    // [[1, 2, 3], [3, 1, 3], [3, 2, 3], [3, 2, 5]],
    // [[1, 2, 3, 3], [3, 1, 2, 2], [3, 1, 2, 1]],
    [[6, 28, 37, 34, 12, 30, 43, 35, 6], [21, 47, 38, 14, 31, 49, 11, 14, 49], [6, 12, 35, 17, 17, 2, 45, 27, 43], [34, 41, 30, 28, 45, 24, 50, 20, 4]]
].map(testcase => console.log(differenceOfDistinctValues(testcase)));