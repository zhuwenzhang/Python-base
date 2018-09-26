class Stack:
    def __init__(self):
        self.__elements = []

    def isEmpty(self):
        return len(self.__elements) == 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements)-1]

    def push(self,value):
        self.__elements.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()

    def getSize(self):
        return len(self.__elements)

