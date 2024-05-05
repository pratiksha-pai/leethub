class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for curr_start, curr_end in self.events:
            if start < curr_end and end > curr_start:
                return False
            
        self.events.append((start, end))
        self.events.sort(key=lambda x:x[0])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)