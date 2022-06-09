// https://leetcode.com/problems/valid-mountain-array

class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int n = arr.size();
        cout<<"n is "<<n<<endl;
        if(n<3) {
            cout<<"n is chota"<<endl;
            return false;
        }
        bool increase = true;
        bool decrease = false;
        int peak = 0;
        for(int i=1; i<n-1; i++){
            cout<<"for i "<<i<<endl;
            if(arr[i]>arr[i-1] && arr[i]>arr[i+1]){
                if(peak==0) {
                    cout<<"1"<<endl;
                    peak=i;
                    decrease = !decrease;
                    increase = !increase;
                }
                else {
                    cout<<"2"<<endl;
                    return false;
                }
            } 
            else{
                if(arr[i]==arr[i-1] || arr[i]==arr[i+1]) {
                    cout<<"3 "<< i <<endl;
                    return false;
                }
                if(increase && arr[i] > arr[i+1] ) {
                    cout<<"4 "<< i <<endl;
                    return false;
                }
                if(decrease && arr[i] < arr[i+1] ) {
                    cout<<"5  "<< i <<endl;
                    return false;
                } 
            }
        }
        if(peak != 0){
            if(arr[0]>arr[1]){
                cout<<"6"<<endl;
                return false;  
            } 
            if(arr[n-1]>arr[n-1]){
                cout<<"7 "<<endl;
                return false;  
            }
        } 
        if(peak == 0) return false;

        return true;
    }
};