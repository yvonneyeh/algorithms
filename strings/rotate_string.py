s1 = 'helloworld'
s2 = 'worldhello'

s3 = 'waterbottle'
s4 = 'bottlewater'

s5 = 'watertable'
s6 = 'bottlewater'

def is_rotated_string(s1, s2):

    if len(s1) != len(s2):
        return False

    s3 = s1 + s1
    if s2 in s3:
        return True
    else:
        return False

print(is_rotated_string(s1, s2))
print(is_rotated_string(s3, s4))
print(is_rotated_string(s5, s6))
