// https://leetcode.com/problems/global-and-local-inversions

class Solution {
public:
    bool isIdealPermutation(vector<int>& a) {
        int global_sum = 0;
        int local_sum = 0;
        int n = a.size();
        // for(int i=0; i<n-1; i++){
        //     if(a[i] > a[i+1]) local_sum++;
        // }
        int max = -1;
        
        for(int i=0; i<n-2; i++){
            max = (a[i] > max ? a[i] : max);
            if(max > a[i+2]) return false;
        }
        return true;
    }
};