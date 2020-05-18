class Node:

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __delete__(self, instance):
        print('Deleted Node with data: ', self.data)


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.totalNodes = 0

    def traverse_forward(self):
        if self.totalNodes == 0:
            print('Empty linked list!')
            return None
        currentNode = self.head
        for _ in range(1, self.totalNodes):
            currentNode = currentNode.next
        return currentNode

    def insert(self, data):
        if self.totalNodes == 0:
            self.head = Node(data)
        else:
            lastNode = self.traverse_forward()
            newNode = Node(data)
            lastNode.next = newNode
            newNode.previous = lastNode
            newNode
        self.totalNodes += 1

    def print_forward(self):
        currentNode = self.head
        print('\n\t\tTotal nodes = ', self.totalNodes)
        for _ in range(self.totalNodes):
            print('\t Node data: ', currentNode.data)
            currentNode = currentNode.next

    def traverse_forward_till(self, position):
        if self.totalNodes == 0:
            print('Empty linked list!')
            return None
        if position >= self.totalNodes:
            position = self.totalNodes
        currentNode = self.head
        for _ in range(1, position + 1):
            currentNode = currentNode.next
        return currentNode

    def insert_at(self, data, position):
        if self.totalNodes == 0:
            self.head = Node(data)
        else:
            if position == 0:
                # Current Node is actually head
                newNode = Node(data)
                previousHead = self.head
                self.head = newNode
                newNode.next = previousHead
                previousHead.previous = newNode
            else:
                if position < 0:
                    position = self.totalNodes + position + 1
# here it is +1 because of the logic when position is negative the previous and next changes

                if position > self.totalNodes:
                    self.insert(data)
                    self.totalNodes -= 1
                else:
                    currentNode = self.traverse_forward_till(position)
                    previousNode = currentNode.previous
                    newNode = Node(data)
                    previousNode.next = newNode
                    newNode.previous = previousNode
                    newNode.next = currentNode
                    currentNode.previous = newNode

        self.totalNodes += 1

    def traverse_forward_until(self, data):
        if self.totalNodes == 0:
            print('Empty linked list!')
            return None
        currentNode = self.head
        for _ in range(1, self.totalNodes):
            if currentNode.data == data:
                break
            currentNode = currentNode.next
        return currentNode

    def get_previous_node(self, data):
        myNode = self.traverse_forward_until(data)
        if myNode.previous is not None:
            print('Node: ', myNode.data, ' and previous node: ', myNode.previous.data)
        else:
            print('Node: ', myNode.data, ' and previous node is null')

    def get_next_node(self, data):
        myNode = self.traverse_forward_until(data)
        if myNode.next is not None:
            print('Node: ', myNode.data, ' and next node: ', myNode.next.data)
        else:
            print('Node: ', myNode.data, ' and next node is null')

    def print_nodes_previous_next(self):
        if self.totalNodes == 0:
            print('Empty linked list!')
            return
        currentNode = self.head
        print('\n\t\tTotal nodes = ', self.totalNodes)
        print('\tPrevious:  Null\t\tNode data: ', currentNode.data, '\t\tNext: ', currentNode.next.data)
        for _ in range(1, self.totalNodes - 1):
            currentNode = currentNode.next
            print('\tPrevious: ', currentNode.previous.data, '\t\tNode data: ', currentNode.data, '\t\tNext: ',
                  currentNode.next.data)
        if self.totalNodes > 2:
            currentNode = currentNode.next
            print('\tPrevious: ', currentNode.previous.data, '\t\tNode data: ', currentNode.data, '\t\tNext: Null')

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


myDLL = DoubleLinkedList()
myDLL.insert('Node1')
myDLL.insert('Node2')
myDLL.insert('Node3')
myDLL.insert('Node4')
myDLL.insert('Node5')

myDLL.print_forward()
myDLL.get_previous_node('Node1')
myDLL.print_nodes_previous_next()

myDLL.insert_at('Node6', -3)
myDLL.print_forward()

myDLL.delete('Node6')
myDLL.print_forward()

myDLL.delete_at(-2)
myDLL.print_forward()
