// https://leetcode.com/problems/convert-bst-to-greater-tree

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
private: int sum = 0;
public:
//     TreeNode* next_successor(TreeNode* root){
//         if (root==NULL) return NULL;
//         TreeNode* curr = root;
//         while(curr && curr->left){
//             curr = curr->left;
//         }
//         return curr;
//     }
//     void sum_all(TreeNode* root){
//         if(root==NULL) return;
//         if(root->right) {
//             sum_all(root->right);
//             TreeNode* temp = next_successor(root->right);
//             if(temp!=NULL) root->val += temp->val;
//         }
//         if(root->left) {
//             sum_all(root->left);
//             TreeNode* temp = next_successor(root->left);
//             root->left->val += root->val;
            
//         }
//         return;
//     }

    TreeNode* convertBST(TreeNode* root) {
        if(root ==NULL) return NULL;
        
        convertBST(root->right);
        sum = sum + root->val;
        root->val = sum;
        convertBST(root->left);
        
        
        
        return root;
    }
};