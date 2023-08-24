#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, x;
    cin >> n >> x;
    vector<pair<int, int>> pricesAndPages(n);
    for (int i = 0; i < n; i++)
    {
        cin >> pricesAndPages[i].first;
    }
    for (int i = 0; i < n; i++)
    {
        cin >> pricesAndPages[i].second;
    }
    sort(pricesAndPages.begin(), pricesAndPages.end());
    vector<vector<int>> dp(x + 1, vector<int>(n + 1));

    for (int tempRemPrice = 1; tempRemPrice <= x; tempRemPrice++)
    {
        for (int tempStartIndex = n - 1; tempStartIndex >= 0; tempStartIndex--)
        {
            int notTake = dp[tempRemPrice][tempStartIndex + 1];
            dp[tempRemPrice][tempStartIndex] = notTake;

            if ((tempRemPrice - pricesAndPages[tempStartIndex].first) < 0)
            {
                continue;
            }
            int take = dp[tempRemPrice - pricesAndPages[tempStartIndex].first][tempStartIndex + 1] + pricesAndPages[tempStartIndex].second;

            dp[tempRemPrice][tempStartIndex] = max(
                dp[tempRemPrice][tempStartIndex], take);
        }
    }
    cout << dp[x][0] << endl;
    return 0;
}
