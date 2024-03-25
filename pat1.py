# -*- coding: utf-8 -*-
"""PAT1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pXW_InIqeDhQ1R_3Zcj3rnp0jrhFOxE_

STACK USING LINKED LIST
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        popped = self.head
        self.head = self.head.next
        return popped.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack elements:")
stack.display()

print("Popped element:", stack.pop())
print("Stack elements after popping:")
stack.display()

print("Peeked element:", stack.peek())