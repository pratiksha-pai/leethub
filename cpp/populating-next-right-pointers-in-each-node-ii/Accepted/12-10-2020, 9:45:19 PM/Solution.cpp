// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (root==NULL) return root;
        queue<Node* > q1, q2;
        q1.push(root);
        Node* curr = NULL;
        while(!q1.empty() || !q2.empty()){
            while(!q1.empty()){
                curr = q1.front();
                q1.pop();
                if(curr->left) q2.push(curr->left);
                if(curr->right) q2.push(curr->right);
                cout<<"q1 "<< curr->val <<" ";
                curr->next = !q1.empty() ? q1.front() : NULL;
            }
            cout<<endl;
            while(!q2.empty()){
                curr = q2.front();
                q2.pop();
                if(curr->left) q1.push(curr->left);
                if(curr->right) q1.push(curr->right);
                cout<<"q2 "<< curr->val <<" ";
                curr->next = !q2.empty() ? q2.front() : NULL;
            }
            cout<<endl;
        }
        return root;
    }
};