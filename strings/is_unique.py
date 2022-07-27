# Determine if a string has all unique characters. What if you can't use additional data structures?

def is_unique(s):
    return len(s) == len(set(s))

# O(n)
def is_unique_with_dict(s):
    character_counts = {}
    for character in s:
        if character in character_counts:
            return False
        character_counts[character] = 1
    return True

# O(NlogN)
def is_unique_with_sorting(s):
    sorted = sorted(s)
    last_character = None
    for character in sorted:
        if character == last_character:
            return False
        last_character = character
    return True
