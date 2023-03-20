/*

Concept session : Stacks and Queues

Stacks :
- LIFO - Last In , First Out Implementation
- can be implemented using list/array
- popping from the top


Basic operations :

- peek() : view the topmost element
- pop() : remove the topmost element
- push() : adds onto the topmost element

In case of pop and push ops, topmost element changes
Time complexity : O(1)

Real life examples :

Undo operation :
Pile of books :


Question :

Q: Reverse a linked list using stack

Input :  1->2->3->4->5
Output : 5->4->3->2->1


Edge case/Assumptions/Observation/Counter question :
// Our output needs to be a linked list



Approach :


  # Create a current variable that is initialized to the head of the linked list
  # Loop through the linked list while the current variable is not None
  # As we traverse the list, wwe have to switch the pointers, the references.
  # But we cannot do so without losing reference to the previous node, so we will use a stack to store the previous node


Queues :
FIFO Implementation, First In First Out

Basic operations :
- dequeue(): removes an element from the front
- enqueue() : adds an element to the rear
- peek() : views the frontmost element

Time complexity : O(1)


Question :

Rotate string with a queue by K places

Input : str = "abcdef", k = 2
Output : "cdefab"


Edge case/Assumptions/Observation/Counter question :
// K is never negative
// str is never empty


Approach :
  1. iterate thru string
  2. shift first element, into stack
  3. pop off stack and append to string



  Follow up :
  Design hit counter : https://leetcode.com/problems/design-hit-counter/(queues)
  Decode a string : https://leetcode.com/problems/decode-string/
  Next greater element : super important



  queue = []

  while k > 0:

    letter = input_array.pop(0)
    queue.append(letter)
    reinserted_letter = queue.pop(0)
    input_array.append(reinserted_letter)
    k -= 1

  return input_array

*/

/*
Yvonne

class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

def reverse_linked_list(node):

  if not node:
    return None
  stack = []
  current = node
  while current:
    stack.append(current)
    current = current.next

  current = dummy = Node(0)
  while stack:
    temp = stack.pop()
    current.next = temp
    current = temp.next
  current.next = None

  return dummy.next


def rotate_string(str, k):
  i = 0
  q = []
  while i <= k - 1:
    q.append(str[i])
    i += 1
  while q:
    letter = q.pop(0)
    str.pop(0)
    str += letter

  return str


*/


//Nicholas
class LinkedList {
  constructor(value, next = null) {
    this.value = value
    this.next = next
  }
}
const reverseLinkedList = (head) => {
  if (!head) return head;

  const stack = [];
  let curr = head;
  while (curr) {
    stack.push(curr);
    curr = curr.next;
  }
  //try to break functions into modular functions , adhering to SOLID principles
  const newHead = new LinkedList(0);
  curr = newHead;

  while (stack.length) {
    const node = stack.pop();
    curr.next = node;
    curr = curr.next;
  }
  curr.next = null;
  return newHead.next;
}

const test = new LinkedList(1, new LinkedList(2, new LinkedList(3, new LinkedList(4))))

console.log(reverseLinkedList(test))



function rotateStr(str, k){
  const arr = str.split('');
  while (k > 0) {
   let ch = arr.shift()
    arr.push(ch)
    k--;
  }
   return arr.join('');
}


//Christian

/*
class Node:

  def __init__(value):
    self.value = value
    self.next = None



def reverse_list(head):

  current = head
  stack = []


  while current:


    stack.append(current)
    next = current.next
    prev = stack.pop()
    current.next = prev
    current = next


  current.next = None
  return head
  */
