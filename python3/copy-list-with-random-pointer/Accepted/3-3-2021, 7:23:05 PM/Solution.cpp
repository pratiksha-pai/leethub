// https://leetcode.com/problems/copy-list-with-random-pointer

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head == NULL ) return NULL;
        
        
//         add temp nodes and add next pointer for new ll
        Node* curr_old = head;
        while(curr_old != NULL){
            Node* temp_node = new Node(curr_old->val);
            temp_node->next = curr_old->next;
            curr_old->next = temp_node;
            curr_old = curr_old->next->next; 
            
        }
        
//         add random pointers for new ll
        Node* curr;
        curr = head;
        while(curr != NULL && curr->next != NULL){
            if(curr->random != NULL) curr->next->random = curr->random->next;
            curr = curr->next->next;
        }
        
//         remove links between old and new ll
        curr = head;
        Node* new_head = head->next;
        while(curr != NULL && curr->next != NULL){
            Node* temp = curr->next;
            curr->next = curr->next->next;
            if(temp->next != NULL) temp->next = temp->next->next;
            else  temp->next = NULL;
            curr = curr->next;
        }
        
//         print to debug
        curr = head;
        while(curr != NULL){
            cout<< "curr->val " << curr->val << " (curr->next != NULL) " << (curr->next != NULL) << " (curr->random != NULL) " << (curr->random != NULL) <<endl;
            curr = curr->next;
        }
        return new_head;
    }
};