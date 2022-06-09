// https://leetcode.com/problems/3sum

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for(int i =0; i<n; i++){
            cout<<nums[i] <<" ";
        }
        
        vector<vector<int>> res;
        vector<bool> visited(n, false);
        
        int i = 0;
        int j = n-1;
        // int sum = 0;
        // while(i<j){
        //     sum += nums[i]+nums[j];
        // }
        
        for(i=0; i<n; i++){
            if(i!=0 && nums[i-1] == nums[i]) continue;
            for(j=n-1; j>i; j--){
                if(j>0 && nums[j] == nums[j+1]) continue;
                vector<int> res_loop;
                int sum = nums[i] + nums[j];
                vector<int>::iterator itr = find(nums.begin(), nums.end(), -sum);
                int discovered_node = (itr - nums.begin());
                if( discovered_node == i) continue;
                if(discovered_node == j) continue;
                if(visited[discovered_node]) continue;
                
                if(itr!= nums.end()){
                    
                    
                    res_loop.push_back(nums[i]);
                    res_loop.push_back(nums[j]);
                    res_loop.push_back(nums[discovered_node]);
                    
                    visited[i] = true;
                    visited[j] = true;
                    visited[discovered_node] = true;
                    
                    res.push_back(res_loop);
                }
            }
            
        }
        
        return res;
    }
};