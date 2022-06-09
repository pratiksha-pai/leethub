// https://leetcode.com/problems/valid-mountain-array

class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int n = arr.size();
        if(n<3) return false;
        vector<int> count(n, 0);
        count[1] = 1;
        count[n-1] = 1;
        int count_two = 0;
        for(int i=0; i<n; i++){
            if(arr[i]>arr[i+1]) count[i]++;
            if(arr[i]>arr[i-1]) count[i]++;
            if(count[i] == 2) count_two++;
        }
        if(count_two == 1) return true;
        else return false;
    }
};