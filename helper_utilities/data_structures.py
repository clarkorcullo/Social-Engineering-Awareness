"""
Custom data structures for the Social Engineering Awareness Program
"""

from typing import Any, Optional, List, Dict, Tuple
from abc import ABC, abstractmethod
import heapq

class Node:
    """Base node class for linked data structures"""
    
    def __init__(self, data: Any):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    """Singly linked list implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data: Any) -> None:
        """Add element to end of list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data: Any) -> None:
        """Add element to beginning of list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, data: Any) -> bool:
        """Delete first occurrence of data"""
        if not self.head:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, data: Any) -> Optional[Node]:
        """Search for element in list"""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def to_list(self) -> List[Any]:
        """Convert to Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __len__(self) -> int:
        return self.size
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

class Stack:
    """Stack implementation using list"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item: Any) -> None:
        """Push item onto stack"""
        self.items.append(item)
    
    def pop(self) -> Optional[Any]:
        """Pop item from stack"""
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self) -> Optional[Any]:
        """Peek at top item without removing"""
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self) -> bool:
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self) -> int:
        """Get stack size"""
        return len(self.items)
    
    def clear(self) -> None:
        """Clear all items"""
        self.items.clear()

class Queue:
    """Queue implementation using list"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item: Any) -> None:
        """Add item to queue"""
        self.items.append(item)
    
    def dequeue(self) -> Optional[Any]:
        """Remove and return first item"""
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def front(self) -> Optional[Any]:
        """Get first item without removing"""
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self) -> int:
        """Get queue size"""
        return len(self.items)
    
    def clear(self) -> None:
        """Clear all items"""
        self.items.clear()

class PriorityQueue:
    """Priority queue implementation using heapq"""
    
    def __init__(self):
        self.items = []
        self.counter = 0  # For stable sorting
    
    def push(self, item: Any, priority: int) -> None:
        """Add item with priority"""
        heapq.heappush(self.items, (priority, self.counter, item))
        self.counter += 1
    
    def pop(self) -> Optional[Any]:
        """Remove and return highest priority item"""
        if self.is_empty():
            return None
        return heapq.heappop(self.items)[2]
    
    def peek(self) -> Optional[Any]:
        """Get highest priority item without removing"""
        if self.is_empty():
            return None
        return self.items[0][2]
    
    def is_empty(self) -> bool:
        """Check if priority queue is empty"""
        return len(self.items) == 0
    
    def size(self) -> int:
        """Get priority queue size"""
        return len(self.items)

class BinaryTreeNode:
    """Node for binary tree"""
    
    def __init__(self, data: Any):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """Binary tree implementation"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, data: Any) -> None:
        """Insert data into binary tree"""
        if not self.root:
            self.root = BinaryTreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node: BinaryTreeNode, data: Any) -> None:
        """Recursive helper for insertion"""
        if data < node.data:
            if node.left is None:
                node.left = BinaryTreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def search(self, data: Any) -> Optional[BinaryTreeNode]:
        """Search for data in tree"""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node: BinaryTreeNode, data: Any) -> Optional[BinaryTreeNode]:
        """Recursive helper for search"""
        if node is None or node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)
    
    def inorder_traversal(self) -> List[Any]:
        """Inorder traversal of tree"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: BinaryTreeNode, result: List[Any]) -> None:
        """Recursive helper for inorder traversal"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

class HashTable:
    """Hash table implementation"""
    
    def __init__(self, size: int = 100):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key: Any) -> int:
        """Generate hash for key"""
        return hash(key) % self.size
    
    def insert(self, key: Any, value: Any) -> None:
        """Insert key-value pair"""
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value for key"""
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def delete(self, key: Any) -> bool:
        """Delete key-value pair"""
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        
        return False
    
    def contains(self, key: Any) -> bool:
        """Check if key exists"""
        return self.get(key) is not None
    
    def keys(self) -> List[Any]:
        """Get all keys"""
        result = []
        for bucket in self.table:
            for key, _ in bucket:
                result.append(key)
        return result
    
    def values(self) -> List[Any]:
        """Get all values"""
        result = []
        for bucket in self.table:
            for _, value in bucket:
                result.append(value)
        return result

class GraphNode:
    """Node for graph"""
    
    def __init__(self, data: Any):
        self.data = data
        self.neighbors = {}

class Graph:
    """Graph implementation using adjacency list"""
    
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, data: Any) -> None:
        """Add node to graph"""
        if data not in self.nodes:
            self.nodes[data] = GraphNode(data)
    
    def add_edge(self, from_data: Any, to_data: Any, weight: float = 1.0) -> None:
        """Add edge between nodes"""
        if from_data not in self.nodes:
            self.add_node(from_data)
        if to_data not in self.nodes:
            self.add_node(to_data)
        
        self.nodes[from_data].neighbors[to_data] = weight
    
    def remove_edge(self, from_data: Any, to_data: Any) -> bool:
        """Remove edge between nodes"""
        if from_data in self.nodes and to_data in self.nodes[from_data].neighbors:
            del self.nodes[from_data].neighbors[to_data]
            return True
        return False
    
    def get_neighbors(self, data: Any) -> List[Tuple[Any, float]]:
        """Get neighbors of node"""
        if data in self.nodes:
            return [(neighbor, weight) for neighbor, weight in self.nodes[data].neighbors.items()]
        return []
    
    def bfs(self, start_data: Any) -> List[Any]:
        """Breadth-first search"""
        if start_data not in self.nodes:
            return []
        
        visited = set()
        queue = Queue()
        result = []
        
        queue.enqueue(start_data)
        visited.add(start_data)
        
        while not queue.is_empty():
            current = queue.dequeue()
            result.append(current)
            
            for neighbor, _ in self.get_neighbors(current):
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
        
        return result
    
    def dfs(self, start_data: Any) -> List[Any]:
        """Depth-first search"""
        if start_data not in self.nodes:
            return []
        
        visited = set()
        result = []
        
        def dfs_recursive(node_data: Any):
            visited.add(node_data)
            result.append(node_data)
            
            for neighbor, _ in self.get_neighbors(node_data):
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_data)
        return result

