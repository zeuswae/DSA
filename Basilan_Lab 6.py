class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def merge(self, list_1, list_2):
        list1 = list_1
        list2 = list_2
        newStack = Stack()

        while not list1.is_empty() and not list2.is_empty():
            if list1.peek() <= list2.peek():
                newStack.push(list1.pop())
            else:
                newStack.push(list2.pop())

        while not list1.is_empty():
            newStack.push(list1.pop())

        while not list2.is_empty():
            newStack.push(list2.pop())

        current_node = newStack.top
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print("")

    def size(self):
        current_node = self.top
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count


print("List 1")
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(4)
stack1.push(5)
stack1.print_stack()

print("\nList 2")
stack2 = Stack()
stack2.push(1)
stack2.push(3)
stack2.push(4)
stack2.print_stack()

print("\nMerged Stack")
stack_merge = Stack()
stack_merge.merge(stack1, stack2)
