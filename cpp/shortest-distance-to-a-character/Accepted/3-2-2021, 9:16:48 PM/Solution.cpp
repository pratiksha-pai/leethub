// https://leetcode.com/problems/shortest-distance-to-a-character

class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        int n = s.size();
        cout<< "n is "<< n<<endl;
        vector<int> vec(n, 0);
        queue<int> index;
        for(int i=0; i<n; i++){
            if(s[i]==c) index.push(i);
        }
        // queue<int>::iterator itr;
        // for(itr=index.begin(); itr!=index.end(); itr++){
        //     cout<<*itr<<endl;
        // }
        // int min_index = index[0];
        // int max_index = index[0];
        // if(index.size()>1){
        //     max_index = index[1];
        // }
        // cout<< "min_index "<< min_index <<endl;
        // cout<< "max_index "<< max_index <<endl;
        cout<< index.size()<<endl;
        int min_index = index.front();
        int max_index = index.front();
        index.pop();
        for(int i=0; i<n; i++){
            cout<<"for i = "<< i << " min_index "<<min_index << " max_index "<< max_index<<endl;
            if(i>max_index){
                min_index = max_index;
                cout<< (!index.empty())<<endl;
                max_index = (!index.empty()) ? index.front(): min_index;
                if(!index.empty()) index.pop();
            }
            cout<<"for i = "<< i << " min_index "<< min_index << " max_index "<< max_index <<endl;
            cout<<endl;
            if(s[i] != c){
                int dist_from_min = abs(i-min_index);
                int dist_from_max = abs(max_index - i);
                vec[i] = (dist_from_min < dist_from_max ) ? dist_from_min : dist_from_max;
            }
        }
        return vec;
    }
};