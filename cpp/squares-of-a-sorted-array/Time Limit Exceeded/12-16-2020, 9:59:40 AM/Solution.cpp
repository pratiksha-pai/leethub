// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n=nums.size();
        // vector<int> squares;
        for(int i=0; i<n; i++){
            nums[i] = nums[i]*nums[i];
            cout<<"for i = "<< i <<" nums[i] = "<<nums[i]<<endl;
        }
//         sorting algorithm
        int i, key, j;  
        for (i = 1; i < n; i++) 
        {  
            key = nums[i];  
            j = i - 1;  

            /* Move elements of arr[0..i-1], that are  
            greater than key, to one position ahead  
            of their current position */
            while (j >= 0 && nums[j] > key) 
            {  
                nums[j + 1] = nums[j];  
                j = j - 1;  
            }  
            nums[j + 1] = key;  
        }
        return nums;
    }
};