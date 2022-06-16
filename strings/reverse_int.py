# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

a = -1234
b = 890
c= 567

def reverse_integer(x):
    string = str(x)

    if string[0] == '-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])

print(reverse_integer(a))
print(reverse_integer(b))
print(reverse_integer(c))
