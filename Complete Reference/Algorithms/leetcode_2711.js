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
        let tlIR = row;
        let tlIC = col;
        for (; tlIR < m && tlIC < n; tlIR++, tlIC++) {
            ans[tlIR][tlIC] = countDistinctInTopLeft.size
            countDistinctInTopLeft.add(grid[tlIR][tlIC]);
        }
        let countDistinctInBottomRight = new Set();
        // let parity = Math.abs(m - n) > 0 ? row : -row;
        tlIR--;
        tlIC--;
        for (;
            (tlIR >= 0 && tlIC >= 0);
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
    [[1, 2, 3], [3, 1, 5], [3, 2, 1]],
    [[1, 2], [3, 1], [3, 2]],
    [[1, 2, 3], [3, 1, 2]]
].map(testcase => console.log(differenceOfDistinctValues(testcase)));