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

print('word:', words, 
    '\nnumber of characters:', number_of_characters, 
    '\nnumber of words:', number_of_words,
    '\nsentence count:', sentence_count,
    '\nlongest word:', longest_word, "- length:", len(longest_word),
    '\nshortest word:', shortest_word, "- length:", len(shortest_word),
    '\nvowel count:', vowel_count)
