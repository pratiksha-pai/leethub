// https://leetcode.com/problems/advantage-shuffle

class Solution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        sort(begin(A), end(A));
        vector<int> tmp = B;
        sort(begin(tmp), end(tmp));
        int idx1 = 0, idx2 = 0, n = size(A);
        unordered_map<int, vector<int> > mp;
        while(idx1 < n)
            if(A[idx1] > tmp[idx2]) mp[tmp[idx2++]].push_back(A[idx1]), A[idx1++] = -1;
            else idx1++;
        for(auto& num : A) if(num != -1) mp[tmp[idx2++]].push_back(num);
        idx2 = 0;
        for(auto& num : B) tmp[idx2++] = mp[num].back(), mp[num].pop_back();
        return tmp;
    }
};