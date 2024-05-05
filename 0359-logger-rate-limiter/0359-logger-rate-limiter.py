class Logger:

    def __init__(self):
        self.events = {}
        

    def shouldPrintMessage(self, t: int, m: str) -> bool:
        if m not in self.events:
            self.events[m] = t
            return True
        else:
            if t - self.events[m] >= 10:
                self.events[m] = t
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)