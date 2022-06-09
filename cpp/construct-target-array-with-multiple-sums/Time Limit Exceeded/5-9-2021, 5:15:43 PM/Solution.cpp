// https://leetcode.com/problems/construct-target-array-with-multiple-sums

class Solution {
public:
    bool isPossible(vector<int>& target) {
        int ans=0;
        while(1){
            sort(target.begin(), target.end());
            int sum = target[target.size()-1];
            int rest=0;
            for(int i=0; i<target.size()-1; i++){
                rest+=target[i];
            }
            if(rest>=sum){
                return false;
            }
            if(sum-rest == 1){
                int flag=0;
                for(int i=0; i<target.size()-1; i++){
                    if(target[i]!=1) flag=1;
                }
                if(flag==0) return true;
            }
            target[target.size()-1]=sum-rest;
        }
        return false;
    }
};