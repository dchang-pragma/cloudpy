class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None # ensure the node is grounded by default

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None # Initially when we construct a list, there are no items
    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
# print(mylist(54))
#Node(31).setData('123')
print(Node(26).getNext())
print(Node(93).getData())
# print(Node(31))
# print(mylist.size())
# print(mylist.search(93))
# print(Node(93).getData())
# print(mylist.search(100))

# mylist.add(100)
# print(mylist.search(100))
# print(mylist.size())

# mylist.remove(54)
# print(mylist.size())
# mylist.remove(93)
# print(mylist.size())
# mylist.remove(31)
# print(mylist.size())
#print(mylist.search(93))

#print(mylist)