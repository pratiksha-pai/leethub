// https://leetcode.com/problems/longest-harmonious-subsequence

class Solution {
public:
    int findLHS(vector<int>& nums) {
        int n = nums.size();
        map<int, int > mp; 
        map<int, int > diff_mp; 
        for (int i = 0; i < n; i++) 
            mp[nums[i]]++; 

        map<int, int >::iterator itr;
        for (itr = mp.begin(); itr!= mp.end(); itr++) {
            diff_mp[itr->first] = 0;
            cout<< itr->first << " " << itr->second << " "<< diff_mp[itr->first]<< "\n";
        }
        for (itr = mp.begin(); (next(itr, 1))!= mp.end(); itr++) {
            // cout << itr->first << " " << itr->second << endl; 
            
            
            cout<< ((next(itr, 1)->first) - (itr->first) == 1) ;
                
            
            // (next(itr, 1)->first) << " "<< (itr->first) << " " << "expression "<< (next(itr, 1)->first) - (itr->first) == 1  << "\n";
            diff_mp[itr->first] = ( (next(itr, 1)->first) - (itr->first) == 1 ) ? ((next(itr, 1)->second) + (itr->second) ) : 0;
        }
        cout << "\n";
        for(itr= diff_mp.begin(); itr!=diff_mp.end(); itr++){
            cout<< itr->first << " " << itr->second << " ";
        }
        int max = 0;
        for(itr= diff_mp.begin(); itr!=diff_mp.end(); itr++){
            if(itr->second > max ) max = itr->second;
            // cout<< itr->first << " " << itr->second << " ";
        }
        cout<< "max is "<< max;
        return max;
    }
};