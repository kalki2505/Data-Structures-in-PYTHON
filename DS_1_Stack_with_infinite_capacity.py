class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        if self.top < 0:
            return True
        else:
            return False

    def push(self, data):
        self.stack += [data]
        self.top += 1

    def pop(self):
        if not self.is_empty():
            popcorn = self.stack[self.top]
            self.stack = self.stack[:self.top]
            self.top -= 1
            return popcorn
        else:
            print('\nERROR: Elements from an empty stack can not be popped out!')

    def print(self):
        print('\n\t\t>>Your stack <<<')
        for i in range(self.top, -1, -1):
            print('\ti = ', i, '\t', self.stack[i])

    def pops(self, times):
        if times <= (self.top+1):
            for _ in range(times):
                self.pop()
        else:
            print('\nError: Elements to be popped are greater than total elements in the stack!')


bookStack = Stack()
print('\n\t\tInitial Stack')
bookStack.push('Book1')
bookStack.push('Book2')
bookStack.push('Book3')
bookStack.push('Book4')
bookStack.push('Book5')
bookStack.push('Book6')
bookStack.push('Book7')
bookStack.push('Book8')
bookStack.push('Book9')
bookStack.push('Book10')
bookStack.print()

print('\n\t\tStack after popping 2 times')
bookStack.pop()
bookStack.pop()

print('\n\t\tStack after popping 3 times')
bookStack.pops(3)
bookStack.print()

