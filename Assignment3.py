class Node:
    def __init__(self,inputData):
        self.data = inputData
        self.nextNode = None

    def setData(self,inputData):
        this.data = inputData

    def getData(self):
        return self.data

    def setNextNode(self, inputNode):
        self.nextNode = inputNode
        
    def getNextNode(self):
        return self.nextNode
        
class Linked_List:
    def __init__(self):
        self.firstNode = None
        
    def add(self, data_in):
        newNode = Node(data_in)
        newNode.next = self.firstNode
        self.firstNode = newNode
   
    def insert(self, pos, item):
        newNode = Node(item)
        curNode = self.firstNode
        for i in range(pos -1):
            curNode = curNode.getNextNode()
        followNode = curNode.getNextNode()
        curNode.setNextNode(newNode)
        newNode.setNextNode(followNode)

    def RemoveNode(self, Removekey):
        HeadVal = self.firstNode
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.firstNode = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None

    def search(self, searchKey): 
         
        current = self.firstNode 
        # loop till current not equal to None 
        while current != None: 
            if current.data == searchKey: 
                return True # data found
            current = current.next
        return False

    def isEmpty(self):
        if(self.firstNode is None):
            return(True)
        return(False)

    def size(self):
        counter = 0
        current=self.firstNode
        while(current !=None):
            counter+=1
            current=current.next
        return(counter)

    def append(self, newdata):
        NewNode = Node(newdata)
        if self.firstNode is None:
            self.firstNode=NewNode
            return
        last = self.firstNode
        while(last.next):
            last = last.next
        last.next=NewNode

    def index(self, searchKey):
        current = self.firstNode
        counter = 0
        # loop till current not equal to None 
        while current != None:
            if current.data == searchKey: 
                return counter # data found
            counter += 1
            current = current.next
        return -1

    def insert(self, pos, newdata):
        if pos is None:
            print("no node with position: ", pos)
            return
        NewNode = Node(newdata)
        NewNode.next = pos.next
        pos.next = NewNode
        
    def Listprint(self):
        printval = self.firstNode
        while (printval):
            print(printval.data),
            printval = printval.next

    def pop(self):
        last = self.firstNode
        while(last.next):
            last = last.next
        temp = last.data
        self.RemoveNode(last.data)
        return temp

llist = Linked_List()

e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed") 
e4 = Node("Thur")
e5 = Node("Fri")

llist.add(e1)
llist.append(e2)
llist.append(e3)
llist.append(e5)

llist.insert(llist.head.next.next, e4)

#print(llist.pop())

llist.Listprint()

        
class Stack:
    def __init__(self):
        self.internal_list = []

    def push(self,item):
        self.internal_list.append()

    def pop(self):
        return self.internal_list.pop()
    
    def peek(self):
        return self.internal_list[len(self.internal_list)-1]
        
    def isEmpty(self):
        return internal_list == []
    
    def size(self):
        return len(internal_list)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


    
        
