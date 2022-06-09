// https://leetcode.com/problems/binary-search-tree-iterator

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
class BSTIterator {
public:
    // struct iter_struct {
    //     int val;
    //     TreeNode *next;
    // };

    queue<int> q;
    
    BSTIterator(TreeNode* root) {
        stack<TreeNode *> s; 
        TreeNode *curr = root; 

        while (curr != NULL || s.empty() == false) { 
            while (curr !=  NULL) { 
                s.push(curr); 
                curr = curr->left; 
            } 
            curr = s.top(); 
            s.pop(); 

            cout << curr->val << " "; 
            q.push(curr->val);
            curr = curr->right; 
        }
    }
    
    int next() {
        if(!q.empty()) {
            int temp = q.front();
            q.pop();
            return temp;
        }
        return 0;

    }
    
    bool hasNext() {
        return !q.empty();
    }

};


/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */