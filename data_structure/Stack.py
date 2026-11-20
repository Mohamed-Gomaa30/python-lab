class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None 

class Stack: 
    def __init__(self):
        self.top = None 
        self.size = 0 

    def __len__(self): # done 
        return self.size 

    def __iter__(self):
    
        current = self.top 
        while current is not None: 
            yield current.value

            current = current.next 

    def is_empty(self)->bool: # done 
        return self.size == 0 

    # Push 
    def push(self, value):

        new_node = Node(value) 
        if self.is_empty(): 
            self.top = new_node
        
        else:
            current = self.top 
            new_node.next = current
            self.top = new_node 

        self.size += 1 
            
    # pop
    def pop(self): 

        if self.is_empty():
            return "Stack Is Empty"

        else: 
            popped = self.top
            self.top = popped.next
            popped.next = None 

            del popped

        self.size -= 1 


if __name__ == "__main__": 

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

    for i in stack: 
        print(i)

    print(len(stack))


