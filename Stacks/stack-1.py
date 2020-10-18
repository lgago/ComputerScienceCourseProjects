'''Stack file written by Luis Gago for CS2420. No help from other students'''
class Stack():
    '''stack class'''
    def __init__(self):
        '''data initializer'''
        self.data = []
        self._size = 0

    def push(self, item):
        '''add items to the end of the stack'''
        self.data.append(item)
        self._size += 1

    def pop(self):
        '''pop of the last element'''
        if self._size == 0:
            raise IndexError()
        self._size -= 1
        return self.data.pop()

    def peek(self):
        '''peek at the last element'''
        if self._size == 0:
            raise IndexError()
        return self.data[-1]

    def clear(self):
        '''clear the entire stack'''
        self.data = []
        self._size = 0

    def size(self):
        '''return the size of the stack'''
        return self._size

    def __str__(self):
        '''allow the stack to be printed'''
        str_val = ""
        for item in self.data:
            str_val += str(item) + " "
        return str_val
