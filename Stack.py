class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} onto the stack.")

    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        print(f"Popped {popped_data} from the stack.")
        return popped_data

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None
