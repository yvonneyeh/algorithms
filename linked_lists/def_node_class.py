#
# Example of a typical, non-recursive class definition in Python
#
class Employee:
  def __init__(self, theFirstName=None, theLastName=None, theAge=None, theDepartment=None):
    self.firstName = theFirstName
    self.lastName = theLastName
    self.age = theAge
    self.department = theDepartment

worker = Employee("Jake", "from StateFarm", 30, "Insurance Agent")
print "This worker's details:", worker.firstName, \
worker.lastName, worker.age, worker.department, "\n\n"



#
# A class definition of a Node. It's made recursive based
# on the object provided in the .next class variable
#
class Node:
  def __init__(self, anyValue=None, nextNode=None):
    self.val = anyValue
    self.next = nextNode



# 5
exampleNode = Node(5, None)
print "The first node's value is:", exampleNode.val, \
"\nThe first node's next pointer points to:", exampleNode.next, "\n\n"



print "Attaching a node to the first node, 5 -> 10"
# 5 -> 10
anotherNode = Node(10, None)
exampleNode.next = anotherNode
print "1. The first node's value is:", exampleNode.val, \
"\n2. Now, the first node's next pointer points to:", exampleNode.next, \
"\n3. The value in the next node is:", exampleNode.next.val, "\n\n"



print "Initializing a linked list with 2 nodes using the constructor:"
# 15 -> 20
noodle = Node(15, Node(20))
print "1. The first node's value is:", noodle.val, \
"\n2. The first node's next pointer points to a node with value:", noodle.next.val, "\n\n"



print "Initializing a linked list with 5 nodes by nesting constructors:"
# 30 -> 31 -> 32 -> 33 -> 34 -> 35
head = Node(30, Node(31, Node(32, Node(33, Node(34, Node(35))))))
print "1. The first node is usually called the 'head'.\
\n2. Meticulously printing out the linked list starting from the head:\n\t", \
 str(head.val) + " ->", \
 str(head.next.val) + " ->", \
 str(head.next.next.val) + " ->", \
 str(head.next.next.next.val) + " ->", \
 str(head.next.next.next.next.val) + " ->", \
 str(head.next.next.next.next.next.val)
print "3. There's nothing valid after the node containing the value 35, it will return 'None':", \
 head.next.next.next.next.next.next, "\n\n"



print "Traversing the linked list more efficiently with a while loop:"
cur = head
while cur:
 print(str(cur.val) + " ->"),
 cur = cur.next # move to the next node

if cur is None:
  print "END_OF_LIST\nReached the end of the LL. There are no more nodes to traverse when cur is None."

#print "\nTrying to access the val field of None will result in an error", \
#head.next.next.next.next.next.next.val
