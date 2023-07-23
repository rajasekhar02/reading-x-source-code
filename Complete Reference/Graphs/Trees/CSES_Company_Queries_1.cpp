#include<bits/stdc++.h>
using namespace std;

vector<int> tree[200001];
int parents_pow_2[200001][20];

void fill_parents(int node, int parent){
    parents_pow_2[node][0] = parent;
    for(int i=1;i<20;i++){
        if (parents_pow_2[node][i-1] != -1)
            parents_pow_2[node][i] = parents_pow_2[parents_pow_2[node][i-1]][i-1];
        else
            parents_pow_2[node][i] = -1;
    }

    for(int i=0;i<tree[node].size();i++){
        if (tree[node][i] == parent){
            continue;
        }
        fill_parents(tree[node][i], node);
    }
}

int ans_query(int node, int parent_at){
    if ((node == -1) || (parent_at == 0)){
        return node;
    }
    for(int i=19;i>-1;i--){
        if ((parent_at) & (1 << i) && parents_pow_2[node][i] != -1){
            return ans_query(parents_pow_2[node][i], parent_at - (1<<i));
        }
    }
    return -1;
}
int main(){
    int n, q;
    cin >> n >> q;
    int temp;
    for(int i = 2; i < n+1; i++){
        cin>>temp;
        tree[i].push_back(temp);
        tree[temp].push_back(i);
    }
    // for(int i=0;i<n;i++){
    //     for(int j=0;j<tree[i].size();j++){
    //         cout<<tree[i][j]<<" ";
    //     }
    //     cout<<endl;
    // }
    fill_parents(1, -1);
    int node = 0;
    int parent_at = 0;
    for(int i=0;i<q;i++){
        cin >> node >> parent_at;
        cout<<ans_query(node, parent_at)<<endl;
    }
    return 0;
}