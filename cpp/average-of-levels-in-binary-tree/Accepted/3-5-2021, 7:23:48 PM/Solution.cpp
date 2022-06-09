// https://leetcode.com/problems/average-of-levels-in-binary-tree

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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> res;
        queue<TreeNode*> q1;
        queue<TreeNode*> q2;
        double node_sum;
        int node_count;
        q1.push(root);
        
        while(!q1.empty() || !q2.empty() ){
            node_sum = 0;
            node_count=0;
            while(!q1.empty()){
                node_count++;
                TreeNode* temp = q1.front();
                node_sum += temp->val;
                q1.pop();
                if(temp->left) q2.push(temp->left);
                if(temp->right) q2.push(temp->right);
            }
            if(node_count!=0) res.push_back(node_sum/node_count);
            
            node_sum = 0;
            node_count=0;
            while(!q2.empty()){
                node_count++;
                TreeNode* temp = q2.front();
                node_sum += temp->val;
                q2.pop();
                if(temp->left) q1.push(temp->left);
                if(temp->right) q1.push(temp->right);
            }
            if(node_count!=0) res.push_back(node_sum/node_count);
            
        }
        return res;
        
    }
};