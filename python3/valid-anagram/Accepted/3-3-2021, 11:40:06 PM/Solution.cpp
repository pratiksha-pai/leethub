// https://leetcode.com/problems/valid-anagram

class Solution {
public:
    bool isAnagram(string s, string t) {
        int s_n =  s.size();
        int t_n =  t.size();
        
        map<char, int> s_anagram;
        map<char, int> t_anagram;
        
        if(s_n != t_n) return false;
        
        for(int i=0; i<s_n; i++){
            s_anagram[s[i]]++;
            t_anagram[t[i]]++;
        }
        
//         map<char, int>::iterator itr;
//         for(itr=s_anagram.begin(); itr!=s_anagram.end(); itr++){
//             cout<< itr->first << " "<< itr->second <<endl;
//         }
        
//         for(itr=t_anagram.begin(); itr!=t_anagram.end(); itr++){
//             cout<< itr->first << " "<< itr->second <<endl;
//         }
        
        map<char, int>::iterator s_itr = s_anagram.begin();
        map<char, int>::iterator t_itr = t_anagram.begin();
        
        while(s_itr!=s_anagram.end() && t_itr!=t_anagram.end()){
            cout<< s_itr->first << " "<< s_itr->second <<endl;
            cout<< t_itr->first << " "<< t_itr->second <<endl;
            if(s_itr->first != t_itr->first) return false;
            if(s_itr->second != t_itr->second) return false;
            s_itr++;
            t_itr++;
            cout<<endl;
        }
        
        return true;
    }
};