# given a linked list , we have to reverse it using recursion approach.
# 1->2->3 => 3->2->1

# defining the class node for the node of the linked list
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

# creating the nodes of the linked list by creating the objects of the class node
node1 = node(5)
node2 = node(6)
node3 = node(8)
node4 = node(2)

# linking the nodes to creat a linked list
node1.next = node2
node2.next = node3
node3.next = node4

# defining the function , we would the return the head of the reversed linked list
def reverse_linked_list(head_node,prev_node):
    # base condition 
    if head_node == None:
        return prev_node
    next_node = head_node.next
    head_node.next = prev_node
    prev_node = head_node
    head_node = next_node
    return reverse_linked_list(head_node,prev_node)
    
# test case
print('Normal linked list before reversing')
temp_node = node1
while temp_node.next != None:
    print(temp_node.data,end = '->')
    temp_node = temp_node.next
print(temp_node.data)
head_node  = node1
prev_node = None
head_after_reverse = reverse_linked_list(head_node,prev_node)


print('Linked List after reversing')
while head_after_reverse.next != None:
    print(head_after_reverse.data,end='->')
    head_after_reverse = head_after_reverse.next
print(head_after_reverse.data)
