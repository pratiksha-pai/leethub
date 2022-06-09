// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left=-1;
        int right=-1;
        bool left_visited = false;
        for(int i=0; i<nums.size(); i++){
            if(nums[i]==target && !left_visited) left_visited=true, left=i, right=i;
            else if(nums[i]==target) right=i;
            else continue;
        }
        if(!left_visited) return {-1, -1};
        vector<int> res;
        res.push_back(left);
        res.push_back(right);
        return res;
        
    }
};