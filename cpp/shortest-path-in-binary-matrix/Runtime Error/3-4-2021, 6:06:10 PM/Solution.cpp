// https://leetcode.com/problems/shortest-path-in-binary-matrix

class Solution {
public:
    // int calculateShortestPath(
    //     vector<vector<int>>& grid, 
    //     int x_start, int x_end, 
    //     int y_start, int y_end)
    // {
    //     if()
    //     return 0;
    // }
    int min_func(int x, int y, int z){
        int min_val = x;
        if(y<min_val) min_val = y;
        if(z<min_val) min_val = z;
        return min_val;
    }
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        // int x_start = 0;
        // int y_start = 0;
        // int x_end = y_end = grid.size();
        int n = grid.size();
        vector< vector<int> > count_vec(n+1, std::vector<int>(n+1, INT_MAX));
        if(grid[0][0] == 1){
            return -1;
        }else count_vec[0][0] = 0;
        
        
        // for(int i=0; i<n;  i++){
        //     for(int i=0; i<n;  i++)
            // if(!grid[0][1]) count_vec[0][i] = 0;
            // if(!grid[1][0]) count_vec[i][0] = 0;
        // }
        
        
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(!grid[i][j]){
                    count_vec[i+1][j+1] = 1 + 
                        min_func(count_vec[i][j+1], count_vec[i+1][j], count_vec[i][j]);
                }else{
                    continue;
                }
            }
        }
        if(count_vec[n][n] == INT_MAX) return -1;
        else return count_vec[n][n];
        // int res = calculateShortestPath(grid, x_start, x_end, y_start, y_end);
        return 0;
    }
};