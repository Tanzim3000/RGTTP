"""
  Lesson 3: ex4.py
"""

# 1. Create your own Shopping List type.
#
# a. Initialize the ShoppingList class with shopping_list
#    shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# b. Add in_list method, that checks if the item is in list or not,
#    use the format() or f-strings to return the string based on truth:
#    - 'apples' is in the shopping list.
#    - 'apples' not in the shopping list.
#
# c. Add special function when printing the list to output:
#    * Replace the list with {} and print using format().
#    My shopping list: ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# d. Add special function for comparison of two objects to output:
#    * Based on the truth.
#    - True
#    - False

# INSERT CODE HERE
shopping_list = ['rice', 'eggs', 'lemons', 'sugar', 'potato']

a.

def in_list(item, shopping_list):
    if item in shopping_list:
        return f"'{item}' is in the shopping list."
    else:
        return f"'{item}' not in the shopping list."

shopping_list = ['rice', 'eggs', 'lemons', 'sugar', 'potato']
item_to_check = 'apples'

result = in_list(item_to_check, shopping_list)
print(result)

b.
def in_list(item, shopping_list):
    if item in shopping_list:
        return "'{}' is in the shopping list.".format(item)
    else:
        return "'{}' not in the shopping list.".format(item)

shopping_list = ['rice', 'eggs', 'lemons', 'sugar', 'potato']
item_to_check = 'apples'

result = in_list(item_to_check, shopping_list)
print(result)

c.

def in_list(item, shopping_list):
    if item in shopping_list:
        return "'{}' is in the shopping list.".format(item)
    else:
        return "'{}' not in the shopping list.".format(item)

def print_formatted_list(lst):
    formatted = "My shopping list: {}".format(lst)
    print(formatted)

shopping_list = ['rice', 'eggs', 'lemons', 'sugar', 'potato']
item_to_check = 'apples'

result = in_list(item_to_check, shopping_list)
print(result)

print_formatted_list(shopping_list)

d.


