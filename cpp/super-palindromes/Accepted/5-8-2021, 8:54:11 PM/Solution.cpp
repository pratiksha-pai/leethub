// https://leetcode.com/problems/super-palindromes

typedef long long ll;
class Solution {
public:
    bool check(ll r) {
        ll save = r;
        ll rev=0;
        while(r){

            rev = 10*rev + r%10;
            r/=10;
        }
        return save==rev;
    }

    int superpalindromesInRange(string left, string right) {

        int limit = 1e5;

        ll x = stoll(left), y = stoll(right);

        int result =0,start=1,ans=0;

        // check for odd length 1234321

        while(start<limit){

            string tmp = to_string(start);
            for(int j=tmp.size()-2;j>=0;j--)
                tmp+=tmp[j];

            ll num = stoll(tmp); // we found our R, now just check if R*2 is a palindrome if yes do ans++;
            num*=num;
            if(num>y) break;
            if(num>=x && check(num)){
                //cout<<num<<endl;
                ans++;
            }

            start++;
        }

        start=1;

        // check for even length 12344321

        while(start<limit){

            string tmp = to_string(start);

            for(int j=tmp.size()-1;j>=0;j--)
                tmp+=tmp[j];

            ll num = stoll(tmp); // we found our R, now just check if R*2 is a palindrome if yes do ans++;
            num*=num;
             if(num>y) break;
            if(num>=x && check(num)){ 
             //   cout<<"EVEN :"<<num<<endl;
                ans++;
            }
            start++;
        }
        return ans;
    }
};