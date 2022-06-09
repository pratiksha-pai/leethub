// https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers

class Solution {
public:
    int minPartitions(string n) {
        int ans = 0;
        for(auto& ch : n) ans = max(ans, ch - '0');
        return ans;
    }
};