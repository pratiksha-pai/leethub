// https://leetcode.com/problems/triangle

class Solution {
public:
    int minfunc(int a, int b){
        if(a<b) return a;
        return b;
    }
    int minimumTotal(vector<vector<int>>& arr) {
        int n=arr.size();
        for(int i=1; i<n; i++){
            for(int j=0; j<=i; j++){
                if(j==0) arr[i][j]+=arr[i-1][j];
                else if(j==i) arr[i][j]+=arr[i-1][j-1];
                else{
                    arr[i][j] += min(arr[i-1][j-1], arr[i-1][j]);
                }
            }
        }
        int min=INT_MAX;
        for(int i=0; i<n; i++){
            for(int j=0; j<=i; j++){
                cout<<arr[i][j]<<" ";
            }
            cout<<endl;
        }
        for(int i=0; i<n; i++){
            if(arr[n-1][i]<min) min=arr[n-1][i];
        }
        return min;
    }
};