// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int count = 0;
        // for(int i=0; i<time.size(); i++){
        //     time[i] = time[i]%60;
        //     cout<< " " << time[i];
        // }

        for(int i=0; i<time.size(); i++){
            for(int j=i+1; j<time.size(); j++){
                if( (time[i]+time[j])%60 == 0) count++;
            }
        }
        return count;
    }
};