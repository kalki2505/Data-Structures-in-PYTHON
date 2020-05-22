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
