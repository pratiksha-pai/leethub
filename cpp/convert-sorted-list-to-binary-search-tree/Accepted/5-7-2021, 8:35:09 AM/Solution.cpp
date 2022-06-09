// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        return ToBST(head,NULL);
    }
    TreeNode* ToBST(ListNode* head, ListNode* tail){
        if(head==tail)
            return NULL;
        ListNode* fast=head;
        ListNode* slow=head;
        while(fast != tail &&fast->next != tail){
            slow=slow->next;
            fast=fast->next->next;
        }
        TreeNode* root=new TreeNode(slow->val);
        root->left=ToBST(head,slow);
        root->right=ToBST(slow->next,tail);
        return root;
    }
    
    
//     TreeNode* util(ListNode **head, int n){        
//         if(n<=0 || *head == NULL) return NULL;
//         TreeNode* left = util(head, n/2);
//         TreeNode* root = new TreeNode();
//         // if(*head == NULL) return NULL;
//         root->val = (*head)->val;
//         root->left=left;
//         *head = (*head)->next;
//         TreeNode* right = util(head, n-n/2);
//         root->right=right;
//         return root;
        
//     }
//     TreeNode* sortedListToBST(ListNode* head) {
//         if(head==NULL) return NULL;
//         int n=0;
//         ListNode* temp = head;
//         while(temp){
//             n++;
//             temp=temp->next;
//         }
//         cout<<"n is "<<n<<endl;
//         TreeNode* root = util(&head, n);
//         return root;
//         return NULL;
//     }
};