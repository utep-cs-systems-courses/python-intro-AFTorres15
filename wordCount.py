# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null
        self.wordCount = 1


# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None


# Code execution starts here Main


# Print linked list
def printlist(llist):
    tmp = llist.head

    while tmp.next is not None:
        print(tmp.data, tmp.wordCount)
        tmp = tmp.next


if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    f = open("speech.txt", "r")
    counter = 0
    # x = f.readline()
    Lines = f.readlines()
    # x = x.split()
    llist.head = Node("first")
    temp = llist.head
    for line in Lines:
        oneLine = line.strip().split()
        for word in oneLine:
            temp.data = word
            temp.next = Node("Temporary")
            temp = temp.next

    printlist(llist)
