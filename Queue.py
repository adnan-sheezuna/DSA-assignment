class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued {data} into the queue.")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:  
            self.rear = None
        print(f"Dequeued {dequeued_data} from the queue.")
        return dequeued_data

    def peek(self):
        if self.front is None:
            print("Queue is empty.")
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None



if __name__ == "__main__":
    
    print("Stack Operations:")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(f"Top element: {stack.peek()}")
    stack.pop()
    stack.pop()
    stack.pop()  

    
    print("\nQueue Operations:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(f"Front element: {queue.peek()}")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()  
