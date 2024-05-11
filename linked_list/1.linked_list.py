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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# # Test the LinkedList
# my_linked_list = LinkedList(4)
# my_linked_list.print_list()

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        return True
    
    def pop(self):
        if self.length ==0:
            return None 
        temp=self.head
        pre= self.head
        while temp.next is not None: 
            pre=temp
            temp=temp.next
        self.tail= pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value
    
# a=LinkedList(1)
# # a.append(3)  
# a.print_list()
# a.append(2)    

# print(a.pop())
# print('rrr')
# print(a.pop())
# print('ss')
# print(a.pop())

    def prepend(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next= self.head
            self.head = new_node
            self.length+=1
            return True

# a=LinkedList(1)
# a.print_list()
# a.prepend(2)
# a.print_list()

    def pop_first(self):
        if self.length==0:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.length-=1
            if self.length==0:
                self.tail= None
        return temp.value

# a=LinkedList(1)
# a.append(2)
# a.append(3)
# a.pop_first()
# print(a.pop_first())
# print(a.pop_first())
# print(a.print_list())
            
    def get(self,index):
        if index < 0 or index >=self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp= temp.next
        return temp.value

# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)

# print(my_linked_list.get(2))

# for set_value this is the approach 1
    def set_value(self,index,value):
        temp=self.head
        if index<0 or index>self.length:
            return None
        for _ in range(index):
            temp=temp.next
        if temp:
            temp.value=value
            return True
        return False

#for set_value this is the approach 2
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
     


# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# print('LL before set_value():')
# my_linked_list.print_list()

# my_linked_list.set_value(1,4)

# print('\nLL after set_value():')
# my_linked_list.print_list()

    def insert(self,index,value):
        
    
my_linked_list =LinkedList(11)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.append(27)

my_linked_list.print_list()
my_linked_list.insert(1,100)
    











