class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Queue: 
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0 

    def __len__(self):
        return self.size

    def __iter__(self):

        current = self.head 
        while current is not None: 
            yield current.value

            current = current.next 

    def is_empty(self): 
        return self.head is None 
    
    def peak(self): 
        if self.is_empty(): 
            return "Queue Is Empty"
        
        return self.head.value

    def enqueue(self, value):

        new_node = Node(value)

        if self.is_empty(): 
            self.head = self.tail =  new_node     
        
        else:
            self.tail.next = new_node
            self.tail = new_node 
            
        self.size += 1 
    
    def dequeue(self): 

        if self.is_empty():
            return "Queue Is Empty"

        current = self.head 
        self.head = current.next

        current.next = None 

        if self.head is None: 
            self.tail = None 

        self.size -=1

        return current.value  


if __name__ == "__main__": 
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print("="*20)
    print("before")
    for i in q: 
        print(i)

    q.dequeue()
    q.dequeue()

    print("="*20)
    print("after")
    for i in q: 
        print(i)