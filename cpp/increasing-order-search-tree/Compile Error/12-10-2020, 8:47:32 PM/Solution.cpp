// https://leetcode.com/problems/increasing-order-search-tree

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
    TreeNode* increasingBST(TreeNode* root) {
        // if(root == NULL) return root;
        if(root->left == NULL && root->right ==NULL) return root;
        else if(root->left == NULL && root->right != NULL) {
            root->right = increasingBST(root->right);
            return root;
        } 
        else if(root->right ==NULL && root->left != NULL) {
            increasingBST(root->left)->right = root;
            root->left = NULL;
            return root;
        }
        else{
            root->right = increasingBST(root->right);
            TreeNode* temp = root->left;
            root->left = NULL;
            increasingBST(temp)->right = root;
        }
        
    }
};