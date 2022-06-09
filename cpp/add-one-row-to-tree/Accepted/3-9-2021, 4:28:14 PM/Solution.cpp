// https://leetcode.com/problems/add-one-row-to-tree

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
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if(root == NULL) return NULL;
        if(d == 1){
            TreeNode* temp = new TreeNode(v);
            temp->left = root;
            root = temp;
        }
        int curr_depth = 1;
        queue<TreeNode*> q1;
        queue<TreeNode*> q2;
        int flag = 0;
        q1.push(root);
        while(!q1.empty() || !q2.empty()){
            if(curr_depth + 1 == d) {
                flag = 0;
                break;
            }
            while(!q1.empty()){
                TreeNode* temp = q1.front();
                q1.pop();
                if(temp->left) q2.push(temp->left);
                if(temp->right) q2.push(temp->right);
            }
            curr_depth++;
            if(curr_depth + 1 == d) {
                flag = 1;
                break;
            }
            while(!q2.empty()){
                TreeNode* temp = q2.front();
                q2.pop();
                if(temp->left) q1.push(temp->left);
                if(temp->right) q1.push(temp->right);
            }
            curr_depth++; 
        }
        if(flag == 0){
//             operations on q1 -> q1 not empty 
            while(!q1.empty()){
                TreeNode* temp = q1.front();
                q1.pop();
                
                TreeNode* left_new_node = new TreeNode(v); 
                left_new_node->left = temp->left;
                temp->left = left_new_node;
                
                TreeNode* right_new_node = new TreeNode(v); 
                right_new_node->right = temp->right;
                temp->right = right_new_node;
                
            }
        }else{
//             operations on q2 -> q2 not empty
            while(!q2.empty()){
                TreeNode* temp = q2.front();
                q2.pop();
                
                TreeNode* left_new_node = new TreeNode(v); 
                left_new_node->left = temp->left;
                temp->left = left_new_node;
                
                TreeNode* right_new_node = new TreeNode(v); 
                right_new_node->right = temp->right;
                temp->right = right_new_node;
                
            }
            
        }
        
        
        
        return root;
    }
};