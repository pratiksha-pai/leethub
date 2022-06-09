// https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal

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
    int vix = 0;
    vector<int> ans;
    void dfs(TreeNode* node, vector<int>& V) {
        if (!node || (ans.size() && ans[0] == -1)) return;
        if (node->val != V[vix++]) ans = {-1};
        else if (node->left && node->left->val != V[vix]) {
            ans.push_back(node->val);
            dfs(node->right, V);
            dfs(node->left, V);
        } else {
            dfs(node->left, V);
            dfs(node->right, V);
        }
    }
public:
    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& V) {
        dfs(root, V);
        return ans;
    }
};