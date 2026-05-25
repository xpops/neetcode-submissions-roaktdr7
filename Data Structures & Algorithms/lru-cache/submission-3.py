    # Hashmap + DoublyLinkedList?
    # * key : Node mapping *

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {} # key : Node pairs
        self.head, self.tail = Node((0, 0)), Node((0, 0))
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # O(1) search: hashmap
        target = self.hashmap.get(key)
        if target:
            # Update the key entry in linkedlist (to be at tail.prev position)
            target.prev.next = target.next
            target.next.prev = target.prev

            target.prev = self.tail.prev
            target.next = self.tail

            target.prev.next = target
            self.tail.prev = target

            return target.data[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        target = self.hashmap.get(key)

        if target: # key already exists
            # update data
            target.data = (key, value)

            # move to back (tail.prev)
            target.prev.next = target.next
            target.next.prev = target.prev

            target.prev = self.tail.prev
            target.next = self.tail

            target.prev.next = target
            self.tail.prev = target

        else: # key doesn't exist
            # create new node, map it, and add to the back
            newNode = Node((key, value))

            self.hashmap[key] = newNode

            newNode.prev = self.tail.prev
            newNode.next = self.tail

            newNode.prev.next = newNode
            self.tail.prev = newNode

            if len(self.hashmap) > self.cap: # exceeds capacity
                # remove from head
                nodeToRemove = self.head.next
                keyToRemove = nodeToRemove.data[0]
                self.head.next = nodeToRemove.next
                if self.head.next:
                    self.head.next.prev = self.head
                self.hashmap.pop(keyToRemove)
