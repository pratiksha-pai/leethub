// https://leetcode.com/problems/determine-if-string-halves-are-alike

class Solution {
public:
    int is_vowel(char s){
        if(s == 'a' || s == 'e' || s == 'i' || s== 'o' || s == 'u') return 1;
        return 0;
    }
    bool halvesAreAlike(string s) {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        cout<<s<<endl;
        int n = s.size();
        int left = 0;
        int right = 0;
        for(int i=0; i<n/2; i++){
            cout<<s[i]<<" ";
            left+= is_vowel(s[i]);
        }
        cout<<endl;
        for(int i=n/2; i<n; i++){
            cout<<s[i]<<" ";
            right+= is_vowel(s[i]);
        }
        cout<<"left "<<left<<" right "<<right<<endl;
        return (left == right);
        
        return false;
    }
};