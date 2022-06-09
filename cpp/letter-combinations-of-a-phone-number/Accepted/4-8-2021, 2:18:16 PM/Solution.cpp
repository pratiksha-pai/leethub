// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if(digits == "") return {};
        int n = digits.size();
        
        map<char, vector<string> > mp;
        mp['2'] = {"a","b","c"};
        mp['3'] = {"d","e","f"};
        mp['4'] = {"g","h","i"};
        mp['5'] = {"j","k","l"};
        mp['6'] = {"m","n","o"};
        mp['7'] = {"p","q","r","s"};
        mp['8'] = {"t","u","v"};
        mp['9'] = {"w","x","y","z"};
        
        
        if(n==1){
            return mp[digits[0]];
        }
        
        vector<string> res = {};
        int m = mp[digits[0]].size();
        // cout<<" m "<<m<<endl;
        for(int i=0; i<m; i++){
            cout<<"mp[digits[0]]["<<i<<"] "<<mp[digits[0]][i] <<endl;
            vector<string> temp = letterCombinations(digits.substr(1, n));
            cout<<"temp size "<<temp.size();
            for(int j=0; j<temp.size(); j++){
                cout<<"temp["<< j << "] " <<temp[j]<<endl;
                res.push_back(mp[digits[0]][i] + temp[j]);
            } 
        }
        return res;
    }
};