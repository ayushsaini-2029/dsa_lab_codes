
#include <iostream>
#include <stack>
using namespace std;

struct Node {
    int data;
    Node *left, *right;
};

Node* create(int x) {
    Node* n = new Node;
    n->data = x;
    n->left = NULL;
    n->right = NULL;
    return n;
}

// Recursive traversals
void inorder(Node* r) {
    if (r == NULL) return;
    inorder(r->left);
    cout << r->data << " ";
    inorder(r->right);
}

void preorder(Node* r) {
    if (r == NULL) return;
    cout << r->data << " ";
    preorder(r->left);
    preorder(r->right);
}

void postorder(Node* r) {
    if (r == NULL) return;
    postorder(r->left);
    postorder(r->right);
    cout << r->data << " ";
}

// Iterative inorder
void iterativeInorder(Node* r) {
    stack<Node*> s;
    Node* p = r;

    while (p != NULL || !s.empty()) {
        while (p != NULL) {
            s.push(p);
            p = p->left;
        }
        p = s.top();
        s.pop();
        cout << p->data << " ";
        p = p->right;
    }
}

// Iterative preorder
void iterativePreorder(Node* r) {
    if (r == NULL) return;

    stack<Node*> s;
    s.push(r);

    while (!s.empty()) {
        Node* p = s.top();
        s.pop();
        cout << p->data << " ";

        if (p->right != NULL) s.push(p->right);
        if (p->left != NULL) s.push(p->left);
    }
}

// Iterative postorder
void iterativePostorder(Node* r) {
    if (r == NULL) return;

    stack<Node*> s1, s2;
    s1.push(r);

    while (!s1.empty()) {
        Node* p = s1.top();
        s1.pop();
        s2.push(p);

        if (p->left != NULL) s1.push(p->left);
        if (p->right != NULL) s1.push(p->right);
    }

    while (!s2.empty()) {
        cout << s2.top()->data << " ";
        s2.pop();
    }
}

int main() {
    Node* root = create(1);
    root->left = create(2);
    root->right = create(3);
    root->left->left = create(4);
    root->left->right = create(5);

    cout << "Inorder: ";
    inorder(root);

    cout << "\nPreorder: ";
    preorder(root);

    cout << "\nPostorder: ";
    postorder(root);

    cout << "\nIterative Inorder: ";
    iterativeInorder(root);

    cout << "\nIterative Preorder: ";
    iterativePreorder(root);

    cout << "\nIterative Postorder: ";
    iterativePostorder(root);

    return 0;
}
