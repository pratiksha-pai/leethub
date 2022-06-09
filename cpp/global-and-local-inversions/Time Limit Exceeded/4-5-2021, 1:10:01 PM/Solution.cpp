// https://leetcode.com/problems/global-and-local-inversions

class Solution {
public:
    bool isIdealPermutation(vector<int>& a) {
        int global_sum = 0;
        int local_sum = 0;
        int n = a.size();
        for(int i=0; i<n-1; i++){
            if(a[i] > a[i+1]) local_sum++;
        }
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                if(a[i] > a[j]) global_sum++;
            }
        }
        return (global_sum == local_sum);
    }
};