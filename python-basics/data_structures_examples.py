# Features Highlighted
# Basic Structures: Lists, tuples, sets, and dictionaries.
# Custom Implementations: Linked lists, stacks, and binary trees.
# Built-in Libraries: collections (defaultdict, Counter, deque) and heapq.
# Advanced Concepts: Graphs and adjacency lists, matrix operations.

# data_structures_examples.py

# 1. Using a list to store and manipulate data
print("1. List operations")
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Add an element
numbers.remove(2)  # Remove an element
print("Updated List:", numbers)

# 2. Using a tuple to store immutable data
print("\n2. Tuple example")
coordinates = (10, 20, 30)
print("Coordinates:", coordinates)
try:
    coordinates[0] = 40  # This will raise an error since tuples are immutable
except TypeError as e:
    print("Error:", e)

# 3. Using a set for unique elements
print("\n3. Set operations")
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")  # Duplicate elements are ignored
fruits.remove("banana")
print("Updated Set:", fruits)

# 4. Using a dictionary to store key-value pairs
print("\n4. Dictionary example")
person = {"name": "Alice", "age": 25, "city": "New York"}
person["age"] = 26  # Update a value
person["profession"] = "Engineer"  # Add a new key-value pair
print("Updated Dictionary:", person)

# 5. Using a stack (list implementation)
print("\n5. Stack implementation using a list")
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print("Stack after pushes:", stack)
stack.pop()  # Pop
print("Stack after pop:", stack)

# 6. Using a queue (deque implementation)
print("\n6. Queue implementation using deque")
from collections import deque
queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
print("Queue after enqueues:", queue)
queue.popleft()  # Dequeue
print("Queue after dequeue:", queue)

# 7. Using a linked list (custom implementation)
print("\n7. Linked list implementation")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print("Linked List:")
ll.display()

# 8. Using a priority queue
print("\n8. Priority queue example")
import heapq
priority_queue = []
heapq.heappush(priority_queue, (2, "Task 2"))
heapq.heappush(priority_queue, (1, "Task 1"))
heapq.heappush(priority_queue, (3, "Task 3"))
print("Priority Queue (min-heap):", priority_queue)
print("Popped element:", heapq.heappop(priority_queue))

# 9. Using a graph (adjacency list)
print("\n9. Graph representation using an adjacency list")
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
print("Graph:", graph)

# 10. Using a binary tree (custom implementation)
print("\n10. Binary tree implementation")
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

# Create a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder Traversal of Binary Tree:")
inorder_traversal(root)

# 11. Using a defaultdict
print("\n\n11. Defaultdict example")
from collections import defaultdict
dd = defaultdict(list)
dd["fruits"]
