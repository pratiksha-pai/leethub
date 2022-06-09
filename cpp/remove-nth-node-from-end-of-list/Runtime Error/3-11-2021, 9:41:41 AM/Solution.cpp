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
        if(head == NULL) return NULL;
        int count = 0;
        ListNode* curr = head;
        while(curr!=NULL){
            count++;
            curr = curr->next;
        }
        cout<<count<<endl;
        ListNode* prev = head;
        curr = head;
        count = count - n;
        while(curr!=NULL && count!=0){
            count--;
            
            prev = curr;
            curr = curr->next;
        }
        // ListNode* temp =  curr;
        prev->next = curr->next;
        delete(curr);
        
        return head;
    }
};