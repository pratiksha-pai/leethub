// https://leetcode.com/problems/integer-to-roman

class Solution {
public:
    string intToRoman(int num) {
        // MDCLXVI
//         1000, 500, 100, 50, 10, 5, 1
        vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string res;
        
        int n = values.size();
        for(int i=0; i<n; i++){
            while(num>=values[i]){
                num -= values[i];
                res += symbols[i];
            }
        }
        return res;
    }
};