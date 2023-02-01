'''
❓ PROMPT
Given an array of strings, combine them into one string, comma separated except for the last two pair, which should be separated with the word "and". We don't want an Oxford comma, so given ["Sam", "Grant", "Jenny"], return "Sam, Grant and Jenny".

Example(s)
commaSeparate(["Daniel", "Craig"]) == "Daniel and Craig"
commaSeparate(["Oliver", "Pixel", "Fido"]) == "Oliver, Pixel and Fido"


🔎 EXPLORE
State your assumptions & discoveries:


Create examples & test cases:


🧠 BRAINSTORM
What approaches could work? Consider data structures or algorithmic patterns.
Analyze the space & time complexity.
Approach 1:
Time: O()
Space: O()


📆 PLAN
High-level outline of approach #:
- count number of strings
- join all strings with a comma separated, except for last one


🛠️ IMPLEMENT
function commaSeparate(names) {
def commaSeparate(names: list[str]) -> str:


🧪 VERIFY
Run your examples & test cases.
Methodically analyze and debug issue(s).

'''

def commaSeparatePythonic(names: list[str]) -> str:

    if not names: return ""
    if len(names) == 1: return names[0]

    commas = [', '.join(names[:-1]), names[-1]]
    result = ' and '.join(commas)

    return result


# iterative
def commaSeparateIterative(names: list[str]) -> str:

    output = []

    for i in range(len(names)):
        if output:
            if i == len(names)-1:
                output.append(" and ")
            else:
                output.append(", ")
        output.append(names[i])

    return ''.join(output)

# recursive
def commaSeparateRecursive(names):
  if not names:
      return ""

  result = ""

  def appendNextVal(index):
    nonlocal result
    if len(names) - index > 0:
      if index == 0:
          result += names[index]
      elif len(names) - index == 1:
          result += ' and ' + names[index]
      else:
          result += ', ' + names[index]

      appendNextVal(index + 1)

  appendNextVal(0)
  return result


print(commaSeparate([]) == "")
print(commaSeparate(["Sophie"]) == "Sophie")
print(commaSeparate(["Daniel", "Craig"]) == "Daniel and Craig")
print(commaSeparate(["Oliver", "Pixel", "Fido"]) == "Oliver, Pixel and Fido")
print(commaSeparate(["Jono", "Paavo", "Tony", "me"]) == "Jono, Paavo, Tony and me")
print(commaSeparate(["John", "John", "John"]) == "John, John and John")
print(commaSeparate(["Sean", "John", "Sean"]) == "Sean, John and Sean")



#
