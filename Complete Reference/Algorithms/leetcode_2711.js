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
    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            let countDistinctInTopLeft = new Set();
            for (let tlIR = row - 1, tlIC = col - 1; tlIR >= 0 && tlIC >= 0; tlIR--, tlIC--) {
                countDistinctInTopLeft.add(grid[tlIR][tlIC]);
            }
            let countDistinctInBottomRight = new Set();
            for (let tlIR = row + 1, tlIC = col + 1; tlIR < m && tlIC < n; tlIR++, tlIC++) {
                // console.log(tlIR,tlIC)
                countDistinctInBottomRight.add(grid[tlIR][tlIC]);
            }
            ans[row][col] = Math.abs(countDistinctInTopLeft.size - countDistinctInBottomRight.size)
        }
    }
    return ans;
};