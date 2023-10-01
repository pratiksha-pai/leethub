class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> mp;
        for (const auto& str: strs){
            unordered_map<char, int> count;
            for (char c: str){
                count[c]++;
            }
            
            vector<pair<char, int>> keyval(count.begin(), count.end());
            sort(keyval.begin(), keyval.end());
            
            string key;
            for (auto& kv : keyval){
                key += kv.first + to_string(kv.second);
            }
            mp[key].push_back(str);
        }
        
        vector<vector<string>> res;
        for (auto& kv : mp){
            res.push_back(kv.second);
        }
        
        return res;
    }
};