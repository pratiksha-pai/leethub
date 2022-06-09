// https://leetcode.com/problems/design-circular-queue

class MyCircularQueue {
public:
    int max_size;
    queue<int> q;
    MyCircularQueue(int k) {
        max_size = k;
    }
    
    bool enQueue(int value) {
        if(q.size() >= max_size) return false;
        q.push(value);
        return true;
    }
    
    bool deQueue() {
        if(q.size() == 0) return false;
        q.pop();
        return true;
    }
    
    int Front() {
        if(q.size() == 0 ) return -1;
        else return q.front();
    }
    
    int Rear() {
        if(q.size() == 0 ) return -1;
        else return q.back();
    }
    
    bool isEmpty() {
        if(q.size() == 0) return true;
        return false;
    }
    
    bool isFull() {
        if(q.size() == max_size) return true;
        return false;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */