// https://leetcode.com/problems/palindrome-linked-list

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head ==NULL) return true;
        if(head->next == NULL) return true;
        ListNode* temp = head;
        vector<int> vec;
        while(temp!=NULL){
            vec.push_back(temp->val);
            temp  = temp->next;
        }
        int n = vec.size();
        for(int i=0; i<n/2; i++){
            if(vec[i] != vec[n-1-i]) return false;
        }
        return true;
    }
};