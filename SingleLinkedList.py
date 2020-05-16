class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __delete__(self, instance):
        print('Deleted Node with data: ', self.data)

    #def __del__(self, instance):
        #print('Deleted Node')


class LinkedList:
    def __init__(self):
        self.head = None
        self.totalNodes = 0

    #    def __init__(self, data):
    #        self.head = Node(data)
    #        self.totalNodes = 1

    def traverse(self):
        if self.totalNodes == 0:
            print('Empty linked list!')
            return None
        else:
            currentNode = self.head
            for _ in range(1, self.totalNodes):
                currentNode = currentNode.next
            return currentNode

    def insert(self, data):
        if self.totalNodes == 0:
            self.head = Node(data)
        else:
            lastNode = self.traverse()
            newNode = Node(data)
            lastNode.next = newNode
        self.totalNodes += 1

    def traverse_till(self, position):
        if position < 0:
            print('Invalid position')
        else:
            if self.totalNodes == 0:
                print('Empty linked list!, total nodes = ', self.totalNodes)
                return None
            else:
                currentNode = self.head
                for _ in range(1, position):
                    #print('Current node data = ', currentNode.data)
                    currentNode = currentNode.next
                return currentNode

    def insert_at(self, data, position):
        if self.totalNodes == 0:
            self.head = Node(data)
        else:
            if position == 0:
                secondNode = self.head
                self.head = Node(data)
                self.head.next = secondNode
            else:
                if position < 0:
                    position = self.totalNodes + position
                if position > self.totalNodes:
                    self.insert(data)
                    self.totalNodes -= 1
                else:
                    beforeNode = self.traverse_till(position+1)
                    afterNode = beforeNode.next
                    #print('before = ', beforeNode.data, ' after = ', afterNode.data)
                    newNode = Node(data)
                    beforeNode.next = newNode
                    newNode.next = afterNode
        self.totalNodes += 1

    def print(self):
        currentNode = self.head
        print('\n\t\tTotal nodes = ', self.totalNodes)
        for _ in range(self.totalNodes):
            print('\t Node data: ', currentNode.data)
            currentNode = currentNode.next

    def delete(self, data):
        if self.totalNodes == 0:
            print('Empty linked list!')

        else:
            currentNode = self.head
            previousNode = None
            found = False
            for _ in range(1, self.totalNodes):
                if currentNode.data == data:
                    found = True
                    break
                previousNode = currentNode
                currentNode = currentNode.next

            if found:
                nextNode = currentNode.next
                if previousNode is not None:
                    previousNode.next = nextNode
                    del currentNode
                else:
                    self.head = nextNode

                self.totalNodes -= 1
            else:
                print('Data: ', data, ' is not found in the linked list')

    def delete_at(self, position):
        if self.totalNodes == 0:
            print('Empty linked list!')
            return
        else:
            if position < 0:
                position = self.totalNodes + position

            if position >= self.totalNodes:
                print('Index out of range')
                return
            else:
                currentNode = self.head
                previousNode = None
                for _ in range(1, position+1):
                    #print('Current node data = ', currentNode.data)
                    previousNode = currentNode
                    currentNode = currentNode.next
                if previousNode is None:
                    head = self.head
                    self.head = self.head.next
                    del head
                else:
                    previousNode.next = currentNode.next
                    del currentNode
                self.totalNodes -= 1


myLL = LinkedList()
myLL.insert('Node1')
myLL.insert('Node2')
myLL.insert('Node3')
myLL.insert('Node4')
myLL.print()
myLL.insert_at('Node5', -2)
myLL.print()
myLL.delete('Node3')
myLL.print()
myLL.delete('Node')
myLL.print()
myLL.delete_at(-2)
myLL.print()
