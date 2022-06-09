// https://leetcode.com/problems/can-place-flowers

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int not_adj=0;
        int m = flowerbed.size();
        if(m==1 && !flowerbed[0]){
            cout<< "im here";
            not_adj++;
        }
        if( m>=2 && !flowerbed[0] && !flowerbed[1] ){
            flowerbed[0] = 1;
            not_adj++;
        }
        for(int i=1; i<m-1; i++){
            if(!flowerbed[i-1] && !flowerbed[i+1] && !flowerbed[i] ) {
                not_adj++;
                flowerbed[i] = 1;
            }
        }
        if( m>=2 && !flowerbed[m-1] && !flowerbed[m-2] ){
            flowerbed[m-1] = 1;
            not_adj++;
        }
        for(int i=0; i<m; i++) cout<< flowerbed[i] << "  ";
        cout<< "not_adj " << not_adj;
        if(not_adj < n) return false;
        else return true;
        
    }
};