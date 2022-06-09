// https://leetcode.com/problems/the-kth-factor-of-n

class Solution {
public:
    int kthFactor(int n, int k) {
        int factor_num = 0;
        for(int i=1; i<=n; i++){
            if(n%i == 0){
                factor_num++;
                if(factor_num == k)
                    return i;
            }
        }
        return -1;
    }
};