// https://leetcode.com/problems/course-schedule-iii

class Solution {
public:
    static int comparator(vector<int> a, vector<int> b){
        return a[1]<b[1];
    }
    int scheduleCourse(vector<vector<int>>& courses) {
        priority_queue<int> p;
        sort(courses.begin(), courses.end(), comparator);
        int prev_end=0;
        for(vector<vector<int>>::iterator it = courses.begin(); it!=courses.end(); it++){
            int duration = (*it)[0];
            int end  = (*it)[1];
            cout<<"duration "<<duration<<" end "<<end<<endl;
            if(prev_end + duration <= end){
                cout<<"loop 1"<<endl;
                prev_end +=duration;
                p.push(duration);
            }else if( !p.empty() && duration<p.top()){
                cout<<"loop 2"<<endl;
                int temp =p.top();
                p.pop();
                prev_end+=duration-temp;
                p.push(duration);
            }
        }
        return p.size();
        
    }
};