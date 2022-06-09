// https://leetcode.com/problems/spiral-matrix-ii

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> gen_matrix(n, vector<int>(n, 0));;
        
        int rtop=0, rbottom=n, cleft=0, cright=n;
        int iter=1;
        
        // for(int i=0; i<n; i++){
        //     for (int j=0; j<n; j++){
        //         cout << gen_matrix[i][j] << " ";
        //     }
        // }
        
        while(rtop<rbottom && cleft<cright){
            
            if( rtop<rbottom && cleft<cright ){
                for(int i=cleft; i<= cright-1; i++){
                    gen_matrix[rtop][i] = iter;
                    iter++;
                }
                rtop++;
            }
            
            if( rtop<rbottom && cleft<cright ){
                for(int i=rtop; i<= rbottom-1; i++){
                    gen_matrix[i][cright-1] = iter;
                    iter++;
                }
                cright--;    
            }

            if( rtop<rbottom && cleft<cright ){
                for(int i=cright-1; i >= cleft; i--){
                    gen_matrix[rbottom-1][i] = iter;
                    iter++;
                }
                rbottom--;
            }
            
            if( rtop<rbottom && cleft<cright ){
                for(int i=rbottom-1; i >= rtop; i--){
                    gen_matrix[i][cleft] = iter;
                    iter++;
                }
                cleft++;   
            }
        }
        return gen_matrix;
    }
};