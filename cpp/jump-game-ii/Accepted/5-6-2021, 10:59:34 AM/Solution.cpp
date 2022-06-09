// https://leetcode.com/problems/jump-game-ii

class Solution {
public:
    int min(int a, int b){
        if(a<b) return a;
        return b;
    }
    int jump(vector<int>& a) {
        int n=a.size();
        vector<int> minjump(n, n+100);
        minjump[0]=0;
        for(int i=1; i<n; i++){
            for(int j=0; j<i; j++){
//                 can i reach the ith position from jth position?
//                 if yes, jump to ith pos is minjump to jth position + 1
                int dist = i-j;
                if(a[j]>=dist){
                    minjump[i]=min(minjump[i], minjump[j]+1);
                }
            }
        }
        for(int i=0; i<n; i++){
            cout<<minjump[i]<<" ";
        }
        cout<<endl;
        return minjump[n-1];
        return 0;
    }
};