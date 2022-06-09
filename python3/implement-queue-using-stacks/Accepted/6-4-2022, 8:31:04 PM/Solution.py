// https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:
    arr = []
    
    def __init__(self):
        self.arr = []
        
    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        temp = None
        if len(self.arr)!=0:
            temp = self.arr[0]
            del self.arr[0]
        return temp

    def peek(self) -> int:
        if len(self.arr)!=0:
            return self.arr[0]

    def empty(self) -> bool:
        if len(self.arr) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()