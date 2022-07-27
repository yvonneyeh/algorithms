# Replace all spaces in a string with '%20'

# Hint: often easiest to mod strings by going from the back to the front

def urlify_pythonic(text, length):
    """solution using standard library"""
    return text.rstrip().replace(' ', '%20')
