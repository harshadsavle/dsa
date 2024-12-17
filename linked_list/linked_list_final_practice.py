class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1


    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
# a=LinkedList(1)
# a.append(10)
# a.print_list()

    def pop(self):
        pre=self.head
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
            return self.head
        temp=self.head.next

        while temp.next is not None:
            temp=temp.next
            pre= pre.next
            if self.length==1:
                self.head=pre
                self.tail=pre
        pre.next=None
        self.length-=1
        return temp
    
# a=LinkedList(1)
# a.append(10)
# a.append(10)

# # a.print_list()


# a.pop()
# a.print_list()

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            temp=self.head
            self.head=new_node
            self.head.next=temp
        self.length+=1
        return True

# a=LinkedList(1)
# a.append(2)
# # a.prepend(0)
# # a.print_list()
# a.pop()
# a.print_list()


    def pop_first(self):
        if self.length==0:
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
        self.length-=1
        return temp.value
    
# a=LinkedList(1)
# a.append(5)
# a.append(10)
# a.pop_first()
# a.print_list()

    def get(self,index):
        if index<0 or index>self.length:
            return False
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

# a=LinkedList(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# print(a.get(0))

    def set_value(self,index,value):
        if index<0 or index>self.length :
            return False
        temp=self.get(index)
        temp.value=value            
        return True

# a=LinkedList(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# a.set_value(1,100)
# a.set_value(2,300)
# a.print_list()
    
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        else:
            new_node=Node(value)
            temp=self.get(index-1)
            next_value=temp.next
            temp.next=new_node
            new_node.next=next_value
        self.length+=1
        return True

# a=LinkedList(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# a.insert(0,100)
# a.print_list()

    def remove(self,index):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.pop_first()
        if index==self.length:
            return self.pop()
        prev=self.get(index-1)
        removed=prev.next
        prev.next=prev.next.next
        removed.next=None
        self.length-=1
        return True
# a=LinkedList(1)
# a.append(2)
# a.append(3)
# a.append(4)
# a.append(5)
# a.remove(4)
# a.print_list()
         
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after=temp.next
        before = None

        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

# Test the LinkedList and the reverse method
a = LinkedList(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
print("Original List:")
a.print_list()
a.reverse()
print("Reversed List:")
a.print_list()