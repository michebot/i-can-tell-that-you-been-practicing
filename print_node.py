
# '''
#     4
#    / \
#   2   5
#  / \   \
# 1   3   6

#   2  
#  / \   
# 1   3 
# '''

class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def __repr__(self):
        return "<Node {data}>".format(data=self.data)
    
one = Node(1)
three = Node(3)
six = Node(6)

two = Node(2, one, three)
five = Node(5, None, six)

four = Node(4, two, five)


def print_in_order(node):
    
    if node.left:
        # print(node.left.data)
        print_in_order(node.left)
    print(node.data)
    if node.right:
        # print(node.right.data)
        print_in_order(node.right)
        

print_in_order(four)






