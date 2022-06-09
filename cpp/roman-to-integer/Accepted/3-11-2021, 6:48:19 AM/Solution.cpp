// https://leetcode.com/problems/roman-to-integer

class Solution {
public:
    int romanToInt(string s) {
        vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int result=0;
        int i=0;
        while(i<s.length())
        {
            if(s[i]=='C' && s[i+1]=='M')
            {
                result +=900;
                i +=2;
            }
            else if(s[i]=='C' && s[i+1]=='D')
            {
                result +=400;
                i +=2;
            }
            else if(s[i]=='X' && s[i+1]=='C')
            {
                result +=90;
                i +=2;
            }
            else if(s[i]=='X' && s[i+1]=='L')
            {
                result +=40;
                i +=2;
            }
            else if(s[i]=='I' && s[i+1]=='X')
            {
                result +=9;
                i +=2;
            }
            else if(s[i]=='I' && s[i+1]=='V')
            {
                result +=4;
                i +=2;
            }
            else if(s[i]=='M')
            {
                result +=1000;
                i +=1;
            }
            else if(s[i]=='D')
            {
                result +=500;
                i +=1;
            }
            else if(s[i]=='C')
            {
                result +=100;
                i++;
            }
            else if(s[i]=='L')
            {
                result +=50;
                i++;
            }
            else if(s[i]=='X')
            {
                result +=10;
                i++;
            }
            else if(s[i]=='V')
            {
                result +=5;
                i++;
            }
            else if(s[i]=='I')
            {
                result +=1;
                i++;
            }
            else
            {
                i++;
            }
        }
        return result;
        
    }
};