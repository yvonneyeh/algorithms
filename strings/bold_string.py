# Add Bold Tag in String

# Given an input string and a query, implement a function `highlight`
# that highlights all occurrences of the query with a bold tag:

# highlight("app", "apple appetizer") => "<b>app</b>le <b>app</b>etizer"

def highlight(query, text):
    text_length = len(s)
    result = []
    bold = [0] * text_length # bold[i] := True if s[i] should be bolded
    bold_end = -1 # s[i:bold_end] should be bolded

    for i in range(text_length):
        if text[i:].startswith(query):
            bold_end = max(bold_end, i + len(text))
        bold[i] = bold_end > i

    i = 0
    while i < text_length:
        if bold[i]:
            j = i
            while j < text_length and bold[j]:
                j += 1 # s[i:j] should be bolded
            result.append('<b>' + text[i:j] + '</b>')
            i = j
        else:
            result.append(s[i])
            i += 1

    return ''.join(result)
