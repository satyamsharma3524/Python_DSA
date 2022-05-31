class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
            
    def pop(self):
        if self.length == 0:
            return None
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        self.tail = curr
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        
        
# creating a linked list with first value of 11
myLinkedList = LinkedList(11)

# appending two items to the list
myLinkedList.append(43)
myLinkedList.append(7)
myLinkedList.print_list()

# removing and pop the last item
myLinkedList.pop()
myLinkedList.print_list()

# adding the new node from front or prepending 
myLinkedList.prepend(56)
myLinkedList.print_list()