// https://leetcode.com/problems/construct-target-array-with-multiple-sums

class Solution {
public:
    bool isPossible(vector<int>& target) {
        if(target.size()==0) return false;
        if(target.size()==1) return target[0]==1;
        
        priority_queue<int> pq(target.begin(), target.end());
        // cout<<accumulate(target.begin(), target.end(), 0)<<endl;
        int sum = accumulate(target.begin(), target.end(), 0);
        int largest=0;
        while(pq.top()!=1){
            
            largest = pq.top();
            pq.pop();
            sum-=largest;
            if(largest<=sum || sum <1) return false;
            
            largest%=sum; //sum+sum+sum+1=largest say 
            sum+=largest;
            pq.push(largest);
            
            
            
            
        }
        
        
        
        
        return true;
    }
};