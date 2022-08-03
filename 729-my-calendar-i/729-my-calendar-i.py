class MyCalendar:

    def __init__(self):
        self.events=[]

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.events)):
            if start<self.events[i][1] and end>self.events[i][0]:
                return False
        
        self.events.append((start, end))
        # self.events.sort(key=lambda x: x[0])
        return True
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)