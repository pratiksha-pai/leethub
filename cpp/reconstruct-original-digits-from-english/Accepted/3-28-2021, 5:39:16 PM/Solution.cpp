// https://leetcode.com/problems/reconstruct-original-digits-from-english

class Solution {
public:
    string originalDigits(string s) {
       vector<string> words = {"zero", "two", "four", "six", "eight", "one", "three", "five", "seven", "nine"};
        vector<int> nums = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};
        vector<int> dChar = {'z', 'w', 'u', 'x', 'g', 'o', 'r', 'f', 'v', 'i'};
        vector<int> cnt(26, 0);
        string res="";
        for(char ch : s){ cnt[ch-'a']++;}
        for(int i = 0; i < 10; i++){
            int count = cnt[dChar[i]-'a'];
            for(char c: words[i])
                cnt[c-'a'] -= count;
            while(count--)
                res += to_string(nums[i]);
        }
        sort(res.begin(), res.end());
        return res;
    }
};