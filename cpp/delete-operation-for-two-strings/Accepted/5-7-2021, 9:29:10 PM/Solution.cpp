// https://leetcode.com/problems/delete-operation-for-two-strings

class Solution {
public:
    int min(int a, int b){
        if(a<b)return a;
        return b;
    }
    int minDistance(string word1, string word2) {
        int n=word1.size();
        int m=word2.size();
        
        vector<vector<int>> dist(n+1, vector<int>(m+1, 0));
        for(int i=0; i<=n; i++){
            // word1 -> i
            
            for(int j=0; j<=m; j++){
                // word2 -> j
                if(i==0 && j==0) continue;
                if(i==0 ||j==0) {
                    dist[i][j]=i+j; 
                    continue;
                }
                if(word1[i-1]==word2[j-1])  dist[i][j]=dist[i-1][j-1];
                else{
                    dist[i][j]=1+min(dist[i-1][j], dist[i][j-1]);
                } 
            }
        }
        
        return dist[n][m];
        return 0;
        
        
    }
};