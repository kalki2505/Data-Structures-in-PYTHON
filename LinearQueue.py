class LinearQueue:

    def __init__(self, capacity):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.capacity = capacity

    def is_full(self):
        if self.rear == self.capacity-1:
            return True
        else:
            return False

    def is_empty(self):
        if self.rear == self.front == -1:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.is_full():
            print('\n\t\tERROR: Queue is full. \"', data, '\" can not be enqueued')
            return
        else:
            if self.is_empty():
                self.front = 0
            self.queue += [data]
            self.rear += 1
            print('\t\"', data, '\" had joined the queue and front, rear = ',self.front, self.rear)

    def dequeue(self):
        if self.is_empty():
            print('\n\t\tERROR: Queue is empty. Dequeuing failed!')
            return
        else:
            data = self.queue[self.front]
            if self.front == self.rear == 0:
                self.front -= 1
            self.queue = self.queue[1:]
            self.rear -= 1
            print('\t\"', data, '\" had left the queue and front, rear = ',self.front, self.rear)

    def print(self):
        if self.is_empty():
            print('\n\t\t>>> Your QUEUE is empty!')
        else:
            print('\n\t\t>>Your queue <<<')
            for i in range(self.front, self.rear+1):
                print('\ti = ', i, '\t', self.queue[i])


booking_queue = LinearQueue(5)
booking_queue.enqueue('Person 1')
booking_queue.enqueue('Person 2')
booking_queue.enqueue('Person 3')
booking_queue.enqueue('Person 4')
booking_queue.enqueue('Person 5')
booking_queue.enqueue('Person 6')
booking_queue.print()
for _ in range(6):
    booking_queue.dequeue()
    booking_queue.print()
