words = input('enter a string: ')
number_of_characters = len(words) 
number_of_words = len(words.split())
sentence_count = len(words.split('.') + words.split('!') + words.split('?')) - 2
word_array = words.split()
# split() looks at the individual words, not cut up

# long word algorithm
longest_word = "" 
for word in word_array:
    if len(word) > len(longest_word):
        longest_word = word # word becomes longest, compare next word, next word longest
# short word algorithm
shortest_word = ""
for word in word_array:
    if shortest_word == "" or len(word) < len(shortest_word):
        shortest_word = word # word becomes shortest, compare next word, next word shortest
# vowel count algorithm
vowel_count = 0
for i in range(len(words)):
    if words[i].lower() in "aeiou": # vowel count per letter, not word
        vowel_count += 1
# dictionary method for counting words
word_count = {}
for word in word_array:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# most common word algorithm
most_common_word = "" # initialize most common word variable
most_common_count = 0 # make the counter start at 0, assign individual count
for word, count in word_count.items(): # word and count are the properties of the word and it's info
    # word_count.items = a tuple that shows properties of that word like it's individual count
    if count > most_common_count:
        most_common_word = word # word becomes most common, compare next word, next word most common
        most_common_count = count # assign the count of the most common word to the counter
    most_common_count = count # assign the count of the most common word to the counter


print('---- TEXT REPORT ----')
print(
    'word:', words, 
    '\nCharacters:', number_of_characters, 
    '\nWords:', number_of_words,
    '\nSentences:', sentence_count,
    '\nLongest word:', longest_word, "- length:", len(longest_word),
    '\nShortest word:', shortest_word, "- length:", len(shortest_word),
    '\nVowels:', vowel_count,
    '\nMost common:', most_common_word, "- count:", most_common_count
    )
print('--------------------')
