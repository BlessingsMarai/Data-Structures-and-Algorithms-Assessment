import string

def word_frequency(sentence):
    # Removing punctuation and converting to lowercase
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    words = sentence.split()
    
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
