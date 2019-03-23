class Node():
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedlist():
    def __init__(self):
        self.headval = None

    def printlist(self):
        printval = self.headval
        while printval:
            print(printval.dataval)
            printval = printval.nextval

    def atBeginning(self,newdata):
        Newnode = Node(newdata)
        if not self.headval:
            self.headval = Newnode
            return
        Newnode.nextval=self.headval
        self.headval=Newnode

    def atEnd(self,newdata):
        Newnode = Node(newdata)
        if not self.headval:
            self.headval = Newnode
            return
        current_node = self.headval
        while current_node.nextval:
            current_node = current_node.nextval

        current_node.nextval = Newnode

    def atMiddle(self,middleNode,newdata):
        Newnode = Node(newdata)

        current_node = self.headval
        while current_node != middleNode:
            current_node = current_node.nextval
        Newnode.nextval = current_node.nextval
        current_node.nextval = Newnode




list1 = SLinkedlist()
list1.headval = Node("Mon")
e1 = Node("Tue")
e2 = Node("Wed")
e3 = Node("Thurs")

list1.headval.nextval=e1
e1.nextval=e2
e2.nextval=e3
list1.atBeginning("Sun")
list1.atEnd("Sat")
list1.atMiddle(e3,"Fri")


list1.printlist()


list2 = SLinkedlist()
list2.atBeginning("1")
list2.atEnd("2")
list2.atEnd("3")
list2.atEnd("4")
list2.atBeginning("0")
list2.printlist()
