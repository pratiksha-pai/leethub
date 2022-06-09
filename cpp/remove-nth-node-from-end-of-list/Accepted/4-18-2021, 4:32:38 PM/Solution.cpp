// https://leetcode.com/problems/remove-nth-node-from-end-of-list

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        ListNode* temp=head;
        int len=0;
        
        while(temp!=NULL){
            len++;
            temp=temp->next;
        }
        if(len==n) return head->next;
        int diff=len-n-1;
        temp=head;
        while(diff){
            temp=temp->next;
            diff--;
        }
        if(temp->next)temp->next=temp->next->next;
        else temp->next=NULL;
        
        
        return head;
    }
};