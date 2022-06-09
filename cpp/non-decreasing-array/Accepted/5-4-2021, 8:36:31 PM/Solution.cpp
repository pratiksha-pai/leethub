// https://leetcode.com/problems/non-decreasing-array

class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int sum = 0;
        int n = nums.size();        
        for(int i = 1; i < n; i++){
            if(nums[i] < nums[i - 1]){
                sum++;
                if(sum >1 ||(i-1>0 && i+1<n && nums[i+1] < nums[i-1] && nums[i] < nums[i-2])) {
                    return false;
                }
            }
        }
        return true;
    }
};