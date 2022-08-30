# Array Slicing

Array slicing involves taking a subset from an array and allocating a new array with those elements.

In Python 3.6 you can create a new list of the elements in my_list, from start_index to end_index (exclusive), like this:

```my_list[start_index:end_index]```

You can also get everything from start_index onwards by just omitting end_index:
```my_list[start_index:]```

Careful: there's a hidden time and space cost here! It's tempting to think of slicing as just "getting elements," but in reality you are:

- allocating a new list
- copying the elements from the original list to the new list

This takes O(n) time and O(n) space, where _nn_ is the number of elements in the resulting list.

That's a bit easier to see when you save the result of the slice to a variable:

  ```tail_of_list = my_list[1:]```

But a bit harder to see when you don't save the result of the slice to a variable:

  ```return my_list[1:]```

Whoops, I just spent O(n) time and space!
```
  for item in my_list[1:]:
    # Whoops, I just spent O(n) time and space!
    pass
```
So keep an eye out. Slice wisely.
