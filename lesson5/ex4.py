"""
  Lesson 5: ex4.py
"""

# 1. Write a function get_index() that returns the index of
#    a character in a string

# INSERT YOUR CODE HERE

def get_index(input_string, char):
    if char in input_string:
        return input_string.index(char)
    else:
        return -1

# Test cases
text = "hello world"
character = "o"
index = get_index(text, character)
if index != -1:
    print(f"The index of '{character}' in the string is: {index}")
else:
    print(f"'{character}' is not in the string.")

# 2. Write a function shout() that returns each word
#  capitalized with "!" and on it's own line.

# INSERT YOUR CODE HERE

def shout(input_string):
    words = input_string.split()
    for word in words:
        capitalized_word = word.capitalize()
        print(f"{capitalized_word}!")
        
# Test
text = "Hello Tanzim how are you?"
shout(text)


# 3. Write a function extract_longer() that extracts
#    words longer or equal to n-characters and return a list,
#    otherwise return False

# INSERT YOUR CODE HERE

def extract_longer(input_string, n):
    words = input_string.split()
    longer_words = [word for word in words if len(word) >= n]
    if longer_words:
        return longer_words
    else:
        return False

# Test
text = "How are you Tanzim?"
n = 4
result = extract_longer(text, n)

if result:
    print("Words longer than or equal to", n, "characters:", result)
else:
    print("No words longer than or equal to", n, "characters found.")