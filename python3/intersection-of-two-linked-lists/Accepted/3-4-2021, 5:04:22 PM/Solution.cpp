// https://leetcode.com/problems/intersection-of-two-linked-lists

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
        int lengthA = 0;
        int lengthB = 0;
        ListNode* currA;
        ListNode* currB;
        
        currA = headA;
        while(currA!=NULL){
            lengthA++; 
            currA = currA->next;
        }
        
        currB = headB;
        while(currB!=NULL){
            lengthB++; 
            currB = currB->next;
        }
        
        currA = headA;
        currB = headB;
        if(lengthA > lengthB){
            int diff = lengthA - lengthB;
            while(diff){
                diff--;
                currA = currA->next;
            }
        }else{
            int diff = lengthB - lengthA;
            while(diff){
                diff--;
                currB = currB->next;
            }
        }
        
        while(currA && currB && currA!=currB){
            currA = currA->next;
            currB = currB->next;
        }
        if(currA == currB){
            return currA;
        }
        else return NULL;
        
    }
};