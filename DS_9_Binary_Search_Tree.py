class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:

    def __init__(self, data):
        self.root = Node(data)

    def insert(self, current, newNode):
        if current.data < newNode.data:
            if current.right is None:
                current.right = newNode
                return current
            self.insert(current.right, newNode)
        elif current.data > newNode.data:
            if current.left is None:
                current.left = newNode
                return current
            self.insert(current.left, newNode)

    def push(self, data):
        return self.insert(self.root, Node(data))

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print('Node data: ', node.data)
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node is not None:
            print('Node data: ', node.data)
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)
            print('Node data: ', node.data)

    def inorder(self):
        print('\n\n\t\t\t>>>INORDER TRAVERSAL')
        self.inorder_traversal(self.root)

    def preorder(self):
        print('\n\n\t\t\t>>>PREORDER TRAVERSAL')
        self.preorder_traversal(self.root)

    def postorder(self):
        print('\n\n\t\t\t>>>POSTORDER TRAVERSAL')
        self.postorder_traversal(self.root)

    def search_node(self, current, data):
        if current.data == data:
            print('Node: ', data, ' found the Binary Search Tree')
            return
        if current.data < data:
            if current.right is None:
                print('Node: ', data, ' is not found the Binary Search Tree')
                return
            else:
                self.search_node(current.right, data)
        elif current.data > data:
            if current.left is None:
                print('Node: ', data, ' is not found the Binary Search Tree')
                return
            else:
                self.search_node(current.left, data)

    def search(self, data):
        print('\n\n\t\t>>> Searching for ', data)
        self.search_node(self.root, data)


# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80

bst = BinarySearchTree(50)
bst.push(30)
bst.push(20)
bst.push(40)
bst.push(70)
bst.push(60)
bst.push(80)
bst.inorder()
bst.preorder()
bst.postorder()
bst.search(10)
bst.search(80)

#Output
"""
			>>>INORDER TRAVERSAL
Node data:  20
Node data:  30
Node data:  40
Node data:  50
Node data:  60
Node data:  70
Node data:  80


			>>>PREORDER TRAVERSAL
Node data:  50
Node data:  20
Node data:  30
Node data:  40
Node data:  60
Node data:  70
Node data:  80


			>>>POSTORDER TRAVERSAL
Node data:  20
Node data:  30
Node data:  40
Node data:  60
Node data:  70
Node data:  80
Node data:  50


		>>> Searching for  10
Node:  10  is not found the Binary Search Tree


		>>> Searching for  80
Node:  80  found the Binary Search Tree

"""
