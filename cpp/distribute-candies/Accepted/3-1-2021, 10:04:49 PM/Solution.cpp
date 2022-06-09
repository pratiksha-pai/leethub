// https://leetcode.com/problems/distribute-candies

class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        set<int, greater<int> > candyTypeSet;
        for(int i=0; i<candyType.size(); i++){
            candyTypeSet.insert( candyType[i] );
        }

        set<int, int>::iterator itr; 
        for (itr = candyTypeSet.begin(); itr != candyTypeSet.end(); ++itr) { 
            cout << *itr  << '\n'; 
        }
        cout<< candyTypeSet.size();
        int ans = 0;
        ans = (candyTypeSet.size() > candyType.size()/2 ) ? candyType.size()/2 : candyTypeSet.size();
        
        return ans;
    }
    
};