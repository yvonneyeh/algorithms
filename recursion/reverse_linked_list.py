"""
/*
1. Given a linked list and an integer, find whether the integer exists in the list. Return a boolean.
2. Given a linked list and an integer, return how many times the integer exists in the list.
3. Find mean of a list of integers
4. Replace all negative values with a 0
5. Reverse the list
*/

class ListNode {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

function listToStr(head) {
  const parts = [];
  while (head) {
    parts.push(head.value);
    head = head.next;
  }
  return "{" + parts.join(" -> ") + "}";
}

"""

class ListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

def reverse(head):
    if head is None:
        return head

    if head.next is None:
        return head

    new_head = reverse_linked_list_recursive(head.next)

    head.next.next = head

    head.next = None


def reverse_linked_list_recursive(head):
    if head is None: # handles empty linked list
        return head

    if head.next is None: # handles linked list with one node
        return head

    # A. label the end node as the new head node
    new_head = reverse_linked_list_recursive(head.next)

    # B. set the new head node's next to be the previous
    #    head node (which is now the end node)
    head.next.next = head

    # C. set the old head node's next to None,
    #    which makes it the end node
    head.next = None


"""
function reverse(head) {
  if (!head || !head.next) {
    return head;
  }
  let tmp = reverse(head.next);
  head.next.next = head;
  head.next = undefined;
  return tmp;
}
"""
