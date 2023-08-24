#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, x;
    cin >> n >> x;
    vector<int> coins(n);
    for (int i = 0; i < n; i++)
    {
        cin >> coins[i];
    }
    sort(coins.begin(), coins.end());
    vector<vector<int>> dp(x + 1, vector<int>(n + 1));
    for (int i = 0; i < n + 1; i++)
    {
        dp[0][i] = 1;
    }
    for (int price = 1; price < (x + 1); price++)
    {
        for (int coinId = 1; coinId < (n + 1); coinId++)
        {
            int notTake = dp[price][coinId - 1];
            dp[price][coinId] = notTake;
            if ((price - coins[coinId - 1]) < 0)
                break;
            int take = dp[price - coins[coinId - 1]][coinId];
            dp[price][coinId] += take;
            dp[price][coinId] = dp[price][coinId] % 1000000007;
        }
    }
    cout << dp[x][n] << endl;
    return 0;
}
