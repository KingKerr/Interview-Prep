"""
Implement a stack that has the following methods:

push(val): push val onto stack

pop: pop off and return topmost element of stack

max: return max value of stack currently.


"""

class MaxStack:
    def__init__(self):
        self.stack = []
        self.maxes = []


    def push(self, val):
        self.stack.append(val)
        if self.maxes:
            self.maxes.append(max(val, self.maxes[-1]))
        else:
            self.maxes.append(val)

    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.maxes[-1]

