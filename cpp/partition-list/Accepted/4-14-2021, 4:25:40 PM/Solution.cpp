// https://leetcode.com/problems/partition-list

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
    ListNode* partition(ListNode* head, int x) {
        
        ListNode* smaller=new ListNode(-1);
        ListNode* smaller_head=smaller; 
        ListNode* greater=new ListNode(-1);
        ListNode* greater_head=greater;
        
        
        ListNode* curr=head;
        ListNode* next=head;
        
        
        while(curr){
            if(curr->val<x) smaller->next=curr, smaller=smaller->next;
            else greater->next=curr, greater=greater->next;
            curr=curr->next;
        }
        
        
        if(smaller)smaller->next=greater_head->next;
        if(greater)greater->next=NULL;
        
        
        return smaller_head->next;
    }
};