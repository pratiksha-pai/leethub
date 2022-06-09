// https://leetcode.com/problems/min-stack

class MinStack:
    arr = []
    
    def __init__(self):
        self.arr = []
        
    def push(self, val: int) -> None:
        self.arr.append(val)
        
    def pop(self) -> None:
        del self.arr[len(self.arr) - 1]

    def top(self) -> int:
        return self.arr[len(self.arr) - 1]
        
    def getMin(self) -> int:
        temp =  [elem for elem in self.arr]
        temp.sort()
        return temp[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()