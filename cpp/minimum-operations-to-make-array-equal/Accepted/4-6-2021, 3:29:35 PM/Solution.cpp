// https://leetcode.com/problems/minimum-operations-to-make-array-equal

class Solution {
public:
    int minOperations(int n) {
//         if even (n-1)*n/2
        if(n%2 == 0){
            cout<<n/2<<endl;
            return ((n/2)*(n/2));
        } 
        else {
            n = (n-1)/2;
            cout<<n<<endl;
            return (n* (n+1));
        }
    }
};