# Find Kth to last element of a singly linked list

# You can traverse through the linked list from head to tail, but you cannot go from the tail to head.

# To find Kth or last node from the linked list List in a single pass:
# 2-pointer approach

# With a singly linked list, the only way to find the end of the list (and Kth node) is to actually iterate all the way to the end.
# The challenge here is attemping to find the solution in only one pass.

# Naive approach: store pointers to each node in an array, allowing us to calculate the n'th from the end once we reach the end
# O(N) extra space, where N is the length of the linked list.

# More efficient -
# keep track of 2 nodes at the same time (loop through list only once)
# pointer 1 starts at head
# pointer 2 starts K nodes ahead of head node
# when p2 reaches the end of the list (null node), p1 will be @ Kth from back

# edge cases:
# - only 1 node
# - empty list
