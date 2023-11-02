noOfNodes = 10

dp = new Array(noOfNodes+1).fill(0)
dp[0] = 1
dp[1] = 1

for(let eachNodeCnt=2;eachNodeCnt<=noOfNodes;eachNodeCnt++){
    for(let pos = 0; pos < eachNodeCnt; pos++){
        dp[eachNodeCnt] += dp[pos]*dp[eachNodeCnt-pos-1]
    }
}

console.log(dp)
