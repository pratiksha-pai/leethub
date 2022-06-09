// https://leetcode.com/problems/n-ary-tree-preorder-traversal

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> res;
    void util(Node* root){
        if(root==NULL) return;
        res.push_back(root->val);   
        int n=0;
        if((root->children).size()!=0) n=(root->children).size();
        for(int i=0; i<n; i++){
            util(root->children[i]);
        }
        return;
    }
    vector<int> preorder(Node* root) {
        if(root==NULL) return {};
        util(root);
        int n=res.size();
        // cout<<"n size "<<n<<endl;
        // for(int i=0; i<n; i++){
        //     cout<<res[i]<<" ";
        // }
        return res;
    }
};