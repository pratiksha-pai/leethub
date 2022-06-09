// https://leetcode.com/problems/binary-tree-right-side-view

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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> right_side;
        queue<TreeNode*> q1, q2;
        if(root == NULL) return {};
        q1.push(root);
        while(!q1.empty() || !q2.empty()){
            while(!q1.empty()){
                TreeNode* temp = q1.front();
                if(q1.size() == 1) right_side.push_back(temp->val);
                q1.pop();
                if(temp->left) q2.push(temp->left);
                if(temp->right) q2.push(temp->right);
            }
            while(!q2.empty()){
                TreeNode* temp = q2.front();
                if(q2.size() == 1) right_side.push_back(temp->val);
                q2.pop();
                if(temp->left) q1.push(temp->left);
                if(temp->right) q1.push(temp->right);
            }
        }
        return right_side;
        
    }
};