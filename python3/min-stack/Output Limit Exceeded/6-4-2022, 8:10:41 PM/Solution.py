// https://leetcode.com/problems/min-stack

class MinStack:
    
    temp_stack = []
    
    def __init__(self):
        self.temp_stack = []
        pass
        
    def push(self, val: int) -> None:
        self.temp_stack.append(val)
        
    def pop(self) -> None:
        if len(self.temp_stack) != 0:
            del self.temp_stack[len(self.temp_stack)-1]
            

    def top(self) -> int:
        return self.temp_stack[len(self.temp_stack)-1]
        
    def getMin(self) -> int:
        # print(type(self.temp_stack))
        # for i in range(len(self.temp_stack)):
        #     print(self.temp_stack[i], end=" ")
        # print()
        
        # temp_stack2 = [elem for elem in self.temp_stack]
        # temp_stack2.append(self.temp_stack.sort())
        # temp_stack2 = temp_stack2.sort()
        temp_stack2 = []
        
        for i in range(len(self.temp_stack)):
            temp_stack2.append(self.temp_stack[i])
            
        print(type(temp_stack2))
        temp_stack2.sort()
        
        for i in range(len(temp_stack2)):
            print(temp_stack2[i], end=" ")
        print()
        
        
        if len(temp_stack2) != 0:
            return temp_stack2[0]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()