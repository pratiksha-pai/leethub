// https://leetcode.com/problems/prefix-and-suffix-search

class WordFilter {
public:
    std::unordered_map <std::string, int> dict;
    WordFilter(vector<string>& words) {
        int index = 0;
        for (std::string word: words) {
            int l = word.length();
            std::vector < std::string > prefix(l + 1, "");
            std::vector < std::string > suffix(l + 1, "");
            for (int i = 1; i <= l; i++) {
                prefix[i] = prefix[i - 1] + word[i - 1];
                suffix[i] = word[l - i] + suffix[i - 1];
            }
            for (int i = 0; i <= l; i++)
                for (int j = 0; j <= l; j++) 
				{
                    std::string key = prefix[i] + '_' + suffix[j];
                    dict[key] = index;
                }
            index+=1;
        }
    }
    
    int f(string prefix, string suffix) {
        {
            std::string key = prefix + "_" + suffix;
            auto it = dict.find(key);
            if (it != dict.end()) return it -> second;
            return -1;
        }  
    }
};

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(prefix,suffix);
 */