// https://leetcode.com/problems/set-mismatch

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        vector<int> nums_correct(n, 0);
        vector<int> return_vector(2, 0);
        int zero_times = 0;
        int two_times = 0;
        for(int i=0; i<n; i++){
            nums_correct[ nums[i]-1]++;
        }
        for(int i=0; i<n; i++){
            cout<< " nums[i] " << nums[i] << " nums_correct[i] " << nums_correct[i] << endl;
        }
        for(int i=0; i<n; i++){
            if(nums_correct[i] == 2) two_times = i+1;
            if(nums_correct[i] == 0) zero_times = i+1;
        }
        return_vector[0] = two_times;
        return_vector[1] = zero_times;
        return return_vector;
        return {};
    }
    
};