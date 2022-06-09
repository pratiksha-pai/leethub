// https://leetcode.com/problems/search-suggestions-system

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(),products.end());
        vector<vector<string>> ans;
        string str;
        for(auto c:searchWord)
        {
            str.push_back(c);
            vector<string> temp;
            auto it = lower_bound(products.begin(),products.end(),str);
            for(int i=0;i<3 and it+i!=products.end();i++)
            {
                string s1 = *(it+i);
                if(s1.find(str))
                    break;
                temp.push_back(s1);
            }
            ans.push_back(temp);
        }
        return ans;
    }
};