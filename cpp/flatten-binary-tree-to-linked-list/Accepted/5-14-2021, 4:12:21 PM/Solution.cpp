// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

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
    void flatten(TreeNode* root) {
        if(root==NULL) return;
        if(root->left == NULL && root->right==NULL) return;
        if(root->right != NULL ) flatten (root->right);
        if(root->left != NULL) flatten(root->left);
        // if(left != NULL) root->right = left; root->left=NULL;
        TreeNode* left = root->left;
        TreeNode* right = root->right;
        if(left!=NULL) root->left = NULL; root->right=left;
        TreeNode* temp = root;
        while(temp->right!=NULL) temp=temp->right;
        temp->right=right;
        
        return;
    }
};