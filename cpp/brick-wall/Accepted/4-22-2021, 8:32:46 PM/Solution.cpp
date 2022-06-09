// https://leetcode.com/problems/brick-wall

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        int rows = size(wall), maxBrickEdges = 0, idx;
        unordered_map<int, int> edgesFrequency; 
        for(auto& row : wall) {
            idx = 0; 
            for(int i = 0; i < size(row) - 1; i++) 
                idx += row[i], edgesFrequency[idx]++;
        }
        for(auto& pair : edgesFrequency) maxBrickEdges = max(maxBrickEdges, pair.second);
        return rows - maxBrickEdges;
    }
};