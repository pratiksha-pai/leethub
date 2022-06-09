// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

class Solution {
public:
    int numberOfSteps (int num) {
        int step_count = 0;
        while(num!= 0){
            if(num%2 == 0) {
                num = num/2;
                step_count++;
            }else{
                num--;
                step_count++;
            }
        }
        return step_count;
    }
};