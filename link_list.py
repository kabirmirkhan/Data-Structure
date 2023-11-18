class Node:
    def __init__(self,value):
        self.value = value
        self.next_add = None

class Link_List:
    def __init__(self,head):
        self.head = head

    def b_insert(self,value):

        new_node = Node(value)
        new_node.next_add = self.head
        self.head = new_node

    def e_insert(self,value):
        new_node = Node(value)

        temp = self.head
        while temp.next_add:
            temp = temp.next_add
        else:
            temp.next_add = new_node

    def m_insert(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
            



first = Node(15)
my_list = Link_List(first)

# my_list.b_insert(9)
my_list.e_insert("UKH")

print(" Value of Head ", my_list.head.value)
print(" Value of Next Address ", my_list.head.next_add)
print(" Value of the Last Node ", my_list.head.next_add.value)

