
# Node class 
class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList: 

    def __init__(self): 
        self.head = None
        self.size = 0 

    def __len__(self):
            return self.size 
    
    def __str__(self):

        if self.head is None: 
            return "LinkedList([])"

        values = []
        current = self.head 

        while current is not None: 
            values.append(str(current.value))
            current = current.next
    
        return f"LinkedList([{', '.join(values)}])"

    def __iter__(self):

        current = self.head 
        while current is not None: 
            yield current.value

            current = current.next 

    def __contains__(self, value):

        current = self.head 
        while current is not None: 
            if current.value == value: 
                return True 
            current = current.next 
            
        return False   

    def __getitem__(self, index):

        if index < 0: 
            index += self.size
            
        if index > self.size: 
            return "Index Out Of Range"

        current = self.head 

        for _ in range(index): 
            current = current.next 

        return current.value

    def __setitem__(self, index, value):

        if self.head is None: 
            return "List is Empty"
        
        if index < 0: 
            index += self.size
            
        if index > self.size: 
            return "Index Out Of Range"
        
        new_node = Node(value)

        prev = self.head 

        for _ in range(index-1): 
            prev = prev.next 

        new_node.next = prev.next 
        prev.next = new_node

        self.size+=1 

    def __delitem__(self, index):
        
        if self.head is None: 
            return "Empty List"

        if index < 0: 
            index += self.size

        if index > self.size: 
            return "Index Out Of Range"

        prev = self.head 

        if index == 0:
            temp = prev.next  
            prev.next = None 
            self.head= temp 
            
        else:

            for _ in range(index-1): 
                prev = prev.next 

            removed = prev.next 
            temp = removed.next
            prev.next = temp 
            
            del temp

        self.size-=1 

    def append(self, node: Node): 
        
        if self.head is None: 
            self.head = node
        else: 
            current = self.head 
            while current.next: 
                current = current.next 

            current.next = node

        self.size += 1 
            
    def prepend(self, node: Node): 

        node.next = self.head
        self.head = node 
        self.size+=1 


if __name__ == "__main__": 

    linkedlist = LinkedList()

    node1  = Node(1)
    node2  = Node(2)
    node3  = Node(3)

    linkedlist.append(node1)
    linkedlist.append(node2)
    linkedlist.append(node3)

    print(f"contains: {1 in linkedlist}")
    print(f"content: {linkedlist}")
    print(f"size of list: {len(linkedlist)}")

    i = -1
    try: 
        print(f"value of index {i}: {linkedlist[i]}")
    except Exception as e:
        print(e) 

    print("=" *20)
    print("before")

    print("Iter:")
    for i in linkedlist: 
        print(i)


    print("=" *20)
    print("after")

    linkedlist[1] = 101
    linkedlist[2] = 102
    linkedlist[3] = 103

    print("Iter:")
    for i in linkedlist: 
        print(i)


    print("=" *20)
    print("after deleting")

    del linkedlist[0]
    del linkedlist[-1]
    
    for i in linkedlist: 
            print(i)


    
    