// https://leetcode.com/problems/missing-number

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int actual_sum = n * (n+1);
        actual_sum = actual_sum/2;
        
        int got_sum = 0;
        for(int i=0; i<n; i++){
            got_sum += nums[i];
        }
        return (actual_sum - got_sum);
    }
};