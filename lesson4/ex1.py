"""
  Lesson 4: ex1.py
"""

# 1. Create 'fruits' dictionary and add following key: values
# apple: 10
# orange: 2

# INSERT YOUR CODE HERE
fruits = {
    'apple': 10,
    'orange': 2
}

print(fruits)

# 2. Add banana to the dictionary and set it's value to 3

# INSERT YOUR CODE HERE

fruits = {
    'apple': 10,
    'orange': 2
}

fruits['banana'] = 3

print(fruits)

# 3. Add mandarin using dictionary method .update()

# INSERT YOUR CODE HERE

fruits = {
    'apple': 10,
    'orange': 2,
    'banana': 3
}

fruits.update({'mandarin': 5})

print(fruits)

# 4. Remove the mandarin from the dictionary

# INSERT YOUR CODE HERE

fruits = {
    'apple': 10,
    'orange': 2,
    'banana': 3,
    'mandarin': 5
}

del fruits['mandarin']

print(fruits)

# 5. Add 10 more apples and remove 2 bananas

# INSERT YOUR CODE HERE

fruits = {
    'apple': 10,
    'orange': 2,
    'banana': 3
}

# Add 10 more apples
fruits['apple'] += 10

# Remove 2 bananas
fruits['banana'] -= 2

print(fruits)

# 6. Remove 'apple' from the dictionary using .pop()
#    and save it's value into a variable 'apples'

# INSERT YOUR CODE HERE

fruits = {
    'apple': 20,
    'orange': 2,
    'banana': 1
}

apples = fruits.pop('apple')

print(fruits)
print("Number of apples:", apples)

# 7. Remove 'mandarin' from the dictionary using .pop()
#    and save it's value into a variable 'mandarin'
#    if 'mandarin' doesn't exist set the variable to 0

# INSERT YOUR CODE HERE

fruits = {
    'apple': 20,
    'orange': 2,
    'banana': 1
}

mandarin = fruits.pop('mandarin', 0)

print(fruits)
print("Number of mandarins:", mandarin)

# 8. Remove last item from the dictionary using .popitem()
#    and save it's value into variable 'last'

# INSERT YOUR CODE HERE

fruits = {
    'apple': 20,
    'orange': 2,
    'banana': 1
}

last_key, last_value = fruits.popitem()

print(fruits)
print("Last item key:", last_key)
print("Last item value:", last_value)

# 9. Check if the 'banana' is in the fruits dictionary.

# INSERT YOUR CODE HERE

fruits = {
    'apple': 20,
    'orange': 2
}

if 'banana' in fruits:
    print("'banana' is in the fruits dictionary.")
else:
    print("'banana' is not in the fruits dictionary.")