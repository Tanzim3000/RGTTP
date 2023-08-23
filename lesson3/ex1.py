"""
  Lesson 3: ex1.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Add banana to a shopping list.

# INSERT CODE HERE

shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']
shopping_list.append('banana')
print(shopping_list)

# 2. Add chocolate in the third position in your shopping list

# INSERT CODE HERE

shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta','banana']
shopping_list.insert(2, 'chocolate')
print(shopping_list)

# 3. Extend shopping list by the following items:
# ['chocolate', 'carrot', 'avocado']

# INSERT CODE HERE
shopping_list = ['apples', 'milk', 'chocolate', 'bread', 'carrot', 'pasta', 'banana']
items_to_add = ['chocolate', 'carrot', 'avocado']
shopping_list.extend(items_to_add)
print(shopping_list)
# 4. Remove first chocolate only

# INSERT CODE HERE
shopping_list = ['apples', 'milk', 'chocolate', 'bread', 'carrot', 'pasta', 'banana', 'chocolate', 'carrot', 'avocado']
shopping_list.remove('chocolate')
print(shopping_list)
# 5. Remove last item from the list

# INSERT CODE HERE
shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta', 'banana', 'chocolate', 'carrot', 'avocado']
last_item = shopping_list.pop()
print("Removed:", last_item)
print("Updated list:", shopping_list)

# 6. Remove third item from the list

# INSERT CODE HERE
shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta', 'banana', 'chocolate', 'carrot', 'avocado']
removed_item = shopping_list.pop(2)
print("Removed:", removed_item)
print("Updated list:", shopping_list)

# 7. Count how many carrots are in the shopping list?

# INSERT CODE HERE

shopping_list = ['apples', 'milk', 'carrot', 'pasta', 'banana', 'chocolate', 'carrot', 'avocado']
carrot_count = shopping_list.count('carrot')
print("Number of carrots:", carrot_count)

# 8. Get the index of the chocolate (careful can throw traceback)

# INSERT CODE HERE
shopping_list = ['apples', 'milk', 'carrot', 'pasta', 'banana', 'chocolate', 'carrot', 'avocado']
chocolate_index = shopping_list.index('chocolate')
print("Index of chocolate:",chocolate_index)
# 9. Get the index of carrot, make sure this code is executed

# INSERT CODE HERE
shopping_list = ['apples', 'milk', 'carrot', 'pasta', 'banana', 'chocolate', 'carrot', 'avocado']
carrot_index = shopping_list.index('carrot')
print("Index of carrot:", carrot_index)


name: str = "Ford Prefect"
name = 100


