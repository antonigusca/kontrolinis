# Create a .txt file with several words.
# Create a function that reads the words from the file and returns the longest word from the file:
# The function should take one parameter - the path to the file/file name.
# The function should return - the longest word from the file.
# Get the longest word using the created function. Print the longest word and its length.

# f = open("words.txt","r")

with open('words.txt', 'r') as f:
   lines = f.read().split(' ')
   



def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(find_longest_word(lines))

# for i in f:
#     print(i)
#
# print(f.read())