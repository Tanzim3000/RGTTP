"""
  Lesson 3: ex3.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Sort the list using built-in function sorted() and print that list

# INSERT CODE HERE

shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']

sorted_shopping_list = sorted(shopping_list)

print(sorted_shopping_list)

# 2. Sort the list using .sort() method and print that list

# INSERT CODE HERE

shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']

shopping_list.sort()

print(shopping_list)

# 3. Use the built-in function reversed(), reverse the list and print that list

# INSERT CODE HERE
shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']

reversed_shopping_list = list(reversed(shopping_list))

print(reversed_shopping_list)
# 4. Reverse the list using sort() method and print the list

# INSERT CODE HERE
shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']

shopping_list.sort(reverse=True)

print(shopping_list)
# 5. Reverse the list using sorted() method and print the list

# INSERT CODE HERE

shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']

reversed_sorted_list = sorted(shopping_list, reverse=True)

print(reversed_sorted_list)