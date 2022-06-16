# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

sentence1 = 'Nice to meet you. My name is Yvonne'
sentence2 ='Something is rotten in the state of Denmark...'

def get_average_word_length(sentence):
    for punctuation in '.!?,;':
        sentence = sentence.replace(punctuation, '')
    words = sentence.split()
    sum_words = sum(len(word) for word in words)
    total_words = len(words)

    return round(sum_words / total_words, 2)

print(get_average_word_length(sentence1))
print(get_average_word_length(sentence2))
