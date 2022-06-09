// https://leetcode.com/problems/add-two-numbers

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = NULL;
        ListNode* curr = NULL;
        ListNode* prev = NULL;
        ListNode* l1_ptr = l1;
        ListNode* l2_ptr = l2;
        int carry = 0;
        while(l1!=NULL || l2!= NULL){
            int sum =0;
            sum += carry;
            if(l1!=NULL){
                sum+= l1->val;
                l1 = l1->next;
            } 
            if(l2!=NULL){
                sum+= l2->val;
                l2 = l2->next;
            }
            carry = sum/10;
            sum = sum%10;
            ListNode* temp = new ListNode;
            temp->val = sum;
            if(head == NULL) head = temp;
            if(curr==NULL && prev==NULL){
                curr = temp;
                prev = temp;
            }else{
                prev = curr;
                curr = temp;
                prev->next = curr;
            } 
        }
        if(carry){
            ListNode* temp = new ListNode;
            temp->val = carry;
            if(head == NULL) head = temp;
            if(curr==NULL && prev==NULL){
                curr = temp;
                prev = temp;
            }else{
                prev = curr;
                curr = temp;
                prev->next = curr;
            }
        }
        return head;
    }
};