// https://leetcode.com/problems/two-sum

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> nums_inverted(n, 0);
        int left =0;
        int right=0;
        for(int i=0; i<n; i++){
            nums_inverted[i] = target - nums[i];
            cout<<nums_inverted[i]<<" ";
        }
        for(int i=0; i<n; i++){
            vector<int>::iterator it = std::find (nums.begin(), nums.end(), nums_inverted[i]);
            if((it - nums.begin()) == i) continue;
            if (it != nums.end()){
                cout<<"found at "<<it - nums.begin()<<endl;
                right = it - nums.begin();
                left= i;
                break;
            }
        }
        vector<int> res;
        res.push_back(left);
        res.push_back(right);
        
        return res;
    }
};