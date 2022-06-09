// https://leetcode.com/problems/container-with-most-water

class Solution {
public:
    int min(int a, int b){
        if(a<b) return a;
        return b;
    }
    int maxArea(vector<int>& height) {
        int right = height.size()-1;
        int left = 0;
        int max_water = 0;
        while(left<right){
            if(max_water < (min(height[left], height[right]) * (right-left))){
                max_water = (min(height[left], height[right]) * (right-left));
            }
            if(height[left]<height[right]) left++;
            else right--;
        }
        return max_water;
    }
};