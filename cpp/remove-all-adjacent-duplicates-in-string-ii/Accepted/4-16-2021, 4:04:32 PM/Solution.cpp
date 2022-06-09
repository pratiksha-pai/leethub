// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution {
public:
    string removeDuplicates(string arr, int k) {
        
        
        int n=arr.size();
        stack<pair<char, int>> s;
        s.push({'#', -1});
        int first, second;
        for(int i=0; i<n; i++){
            // cout<<s.top().first<<" "<<s.top().second<<endl;
            if(s.top().first!=arr[i]) s.push({arr[i], 1});
            else{
//                 if equal;
                s.top().second+=1;
                if(s.top().second==k) {
                    s.pop();
                }
            }
        }
        string str;
        while(!s.empty()){
            cout<<s.top().first<<" "<<s.top().second<<endl;
            if(s.top().second>=1) {
                str+=(s.top().first);
                s.top().second-=1;
            }else s.pop();
        }
        reverse(str.begin(), str.end());
        return str;
    }
};