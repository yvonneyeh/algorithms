# Replace all spaces in a string with '%20'

# Hint: often easiest to mod strings by going from the back to the front

def urlify_pythonic(text, length):
    """solution using standard library"""
    return text.rstrip().replace(' ', '%20')


def urlify_algo(string, length):
  """replace spaces with %20 and removes trailing spaces, assuming the trailing spaces were pusposely put there to make sure that the final string fits in them"""
  # Create an empty array that is sufficiently long
  char_list = [""] * len(string)

  new_index = 0
  for i in range(length):
    next_char = string[i] # Look up in the original string
    if next_char != " ":
      # Put the character in the new position
      char_list[new_index] = next_char
      new_index += 1
    else:
      # Put 3 characters in the new position
      char_list[new_index] = "%"
      char_list[new_index + 1] = "2"
      char_list[new_index + 2] = "0"
      new_index += 3

  # convert back to string
  return "".join(char_list[:new_index])
