// https://leetcode.com/problems/critical-connections-in-a-network

class Solution {
public:
    
    vector<vector<int>> ans; // required answer
    vector<vector<int>> adj; // undirected graph
    vector<int> id; // id number
    vector<int> low; // lowlink value
    vector<int> par; // parent
    int time=0; // time
    
    void dfs(int node){
        id[node]=low[node]=time++; // incrementing time after each node gets visited
        for(int &u:adj[node]) //exploring all the adjacent nodes of node
        {
            if(id[u]==-1) // checking if adjacent node is unvisited
            {
                par[u]=node; // assigning node as parent of adjacent node
                dfs(u); // performing dfs for adjacent node
                low[node]=min(low[node],low[u]); // minimising lowlink value of node
                if(id[node]<low[u]) // checking if we have a bridge yet
                    ans.push_back({node,u});
            }
            else if(u!=par[node]) // checking if adjacent is not parent of node
                low[node]=min(low[node],id[u]); // minimising lowlink value of node
        }
    }
    
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        adj.resize(n);
        par.resize(n,-1);
        low.resize(n,-1);
        id.resize(n,-1);
        for(int i=0;i<connections.size();i++){ // building our graph
            adj[connections[i][0]].push_back(connections[i][1]); 
            adj[connections[i][1]].push_back(connections[i][0]);
        }
        for(int i=0;i<n;i++) // performing dfs on unvisited nodes
        {
            if(id[i]==-1)
                dfs(i);
        }
        return ans;
    }
};