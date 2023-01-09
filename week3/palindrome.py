class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.c
    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        node = Node (data)
        self.count += 1
        # Add a node at the front of the list
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    
    
    
    def addLast(self, data) -> None:
        # Add a node at the end of the list
        node = Node (data)
        self.count += 1
        # Add a node at the front of the list
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node


    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        if index == self.count:
            return self.addLast(data)
        if index == 0:
            return self.addFirst(data)
        if index > self.count:
            return 
        if index < self.count:
            curr = self.head
            counter = 0
            node = Node(data)

            while curr.next != None:
                if counter == index:
                    prev = curr
                    next = curr.next

                    node.prev = prev
                    next.prev = node
                    node.next = next

                    prev.next = node 
                    break
                else:
                    counter += 1
                    curr = curr.next

        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.


    def indexOf(self, data):
            curr = self.head
            counter = 0
            while curr.next != None:
                if curr.data  == data:
                    break
                else:
                    counter += 1
                    curr = curr.next
            return counter
        # Search through the list. Return the index position if data is found, otherwise return -1    



    def add(self, data) -> None:
        # Append an item to the end of the list
            self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr
myList = DoublyLinkedList()
myList.addAtIndex("the",0)
myList.addFirst("May")
myList.addLast("force")
myList.addLast("be")
myList.addLast("with")
myList.addLast("you")
myList.addAtIndex("!",6)
print(myList.__str__())
print(myList.indexOf("with"))
myList.addAtIndex("all",5)
myList.addAtIndex("us",5)
myList.delete("you")
print(myList.__str__())
