# Remove duplicates from an unsorted linked lists

def remove_dupes(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll

# O(N)

# Hint: hash table, should be able to do this in a single pass of the linked lists
# Hint: without extra space, you'll need O(N^2) time. Try using 2 pointers, where the 2nd one searches ahead of the first one.

# What if no temporary buffer is allowed?

def remove_dupes_runner(ll):
    runner = current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    ll.tail = runner
    return ll

# Space: O(1)
# Time: O(N^2)
