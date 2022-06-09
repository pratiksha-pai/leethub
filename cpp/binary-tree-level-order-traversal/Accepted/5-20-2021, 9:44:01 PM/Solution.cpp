// https://leetcode.com/problems/binary-tree-level-order-traversal

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
    void iterate_temp(vector<int> temp){
        if(temp.size()==0) return;
        for(int i=0; i<temp.size(); i++) cout<<temp[i]<<" ";
        cout<<endl;
        return;
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root==NULL) return {};
        queue<TreeNode*> q1, q2;
        q1.push(root);
        vector<vector<int>> res;
        vector<int> temp_vec;
        while(!q1.empty() || !q2.empty()){
            
            while(!q1.empty()){
                TreeNode* temp = q1.front();
                q1.pop();
                temp_vec.push_back(temp->val);
                if(temp->left) q2.push(temp->left);
                if(temp->right) q2.push(temp->right);
            }
            if(temp_vec.size() !=0) res.push_back(temp_vec);
            temp_vec.clear();
            while(!q2.empty()){
                TreeNode* temp = q2.front();
                q2.pop();
                temp_vec.push_back(temp->val);
                if(temp->left) q1.push(temp->left);
                if(temp->right) q1.push(temp->right);
            }
            if(temp_vec.size() !=0) res.push_back(temp_vec);
            temp_vec.clear();
        }
        
        
        return res;
    }
};