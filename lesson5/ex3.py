"""
  Lesson 5: ex3.py
"""

# 1. Write a for loop to iterate over list: [1, 2, 3, 'a', 'b', 'c']

# INSERT YOUR CODE HERE

my_list = [1, 2, 3, 'a', 'b', 'c']
for item in my_list:
    print(item)

# 2. Write for loop to print each character in word "orange"

# INSERT YOUR CODE HERE

word = "orange"
for char in word:
    print(char)

# 3. Using following shopping list:
# shopping_list: ['orange', 'banana', 'mandarin']
# Print "Note to self, buy: " and then iterate
# over each element in the list

# INSERT YOUR CODE HERE

shopping_list = ['orange', 'banana', 'mandarin']
print("Note to self, buy:")
for item in shopping_list:
    print(item)

# 4. Write for loop using range to print numbers from 0 to 10

# INSERT YOUR CODE HERE

for num in range(11):
    print(num)

# 5. Write for loop using range to print numbers from 10 to 20

# INSERT YOUR CODE HERE

for num in range(10, 21):
    print(num)

# 6. Write for loop using range to print even numbers from 10 to 20

# INSERT YOUR CODE HERE

for num in range(10, 21, 2):
    print(num)

# 7. Write for loop using range, to print every 5 numbers
#    down from 100 to 0

# INSERT YOUR CODE HERE

for num in range(100, -1, -5):
    print(num)


# 8. Write for loop using enumerate to print element and it's index

# INSERT YOUR CODE HERE

my_list = ['apple', 'banana', 'cherry', 'date']

for index, element in enumerate(my_list):
    print(f"Index: {index}, Element: {element}")