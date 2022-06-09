// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
//         using sliding window
        unordered_set<char> visited;
        int n = s.size();
        int i, j, ans;
        i= 0; j = 0; ans = 0;
        while(i<n && j<n){
            if(visited.find(s[j]) == visited.end()){
                // cout<<"char "<<s[j]<<" not in the set"<<endl;
                visited.insert(s[j]);
                j++;
                if(ans < (j-i)) ans = (j-i);
            }else{
                // cout<<"char "<<s[j]<<" in the set"<<endl;
                // unordered_set<char>::iterator itr = visited.end();
                // itr--;
                visited.erase(s[i]);
                i++;
            }
            // for (auto it = visited.begin(); it != visited.end(); ++it) 
            //     cout << ' ' << *it;
            // cout<<endl;
        }
        return ans;
    }
};