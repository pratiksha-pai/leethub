// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int count = 0;
        int arr[61] = { 0 };
        for(int i=0; i<time.size(); i++){
            time[i] = time[i]%60;
            arr[time[i]]++;
            cout<< " " << time[i];
        }
        cout << endl;
        for(int i=0; i<60; i++) cout<< "" << arr[i];
        
        for(int i=0; i<=30; i++){
            int x = arr[i];
            if(i==0){
                cout<< "x "<< x;
                count += (x * (x-1))/2;
                cout << "count "<< count;
            } 
            if(i == 30){
                cout<< "x "<< x;
                count += (x * (x-1))/2;
                cout << "count "<< count;
            }
            else count += arr[i] * arr[60-i];
        }
        // for(int i=0; i<time.size(); i++){
        //     for(int j=i+1; j<time.size(); j++){
        //         if( (time[i]+time[j])%60 == 0) count++;
        //     }
        // }
        return count;
    }
};