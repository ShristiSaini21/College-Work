# 1. Write a Python program to create and display a tuple.
'''my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)'''

# 2. Write a program to create a tuple with different data types.
'''mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed Data Types Tuple:", mixed_tuple)'''

# 3. Write a program to find the length of a tuple.
'''my_tuple = (10, 20, 30, 40, 50)
print("Length of tuple:", len(my_tuple))'''

# 4. Write a program to access tuple elements using indexing.
'''my_tuple = ("apple", "banana", "cherry", "date")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])'''

# 5. Write a program to access tuple elements using slicing.
'''my_tuple = (10, 20, 30, 40, 50, 60, 70)
print("Sliced elements (index 1 to 4):", my_tuple[1:5])'''

# 6. Write a program to check if an element exists in a tuple.
'''my_tuple = (10, 20, 30, 40, 50)
element = 30
if element in my_tuple:
    print(f"{element} exists in the tuple")
else:
    print(f"{element} does not exist in the tuple")'''

# 7. Write a program to count the occurrences of an element in a tuple.
'''my_tuple = (1, 2, 3, 2, 4, 2, 5)
print("Occurrences of 2:", my_tuple.count(2))'''

# 8. Write a program to find the index of an element in a tuple.
'''my_tuple = (10, 20, 30, 40, 50)
print("Index of 30:", my_tuple.index(30))'''

# 9. Write a program to concatenate two tuples.
'''tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print("Concatenated Tuple:", result)'''

# 10. Write a program to repeat a tuple n times.
'''my_tuple = (1, 2, 3)
n = 3
print("Repeated Tuple:", my_tuple * n)'''

# 11. Write a program to convert a list into a tuple.
'''my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print("Converted Tuple:", my_tuple)'''

# 12. Write a program to convert a tuple into a string.
'''my_tuple = ('P', 'y', 't', 'h', 'o', 'n')
result_string = "".join(my_tuple)
print("Converted String:", result_string)'''

# 13. Write a program to find the maximum and minimum values in a tuple.
'''my_tuple = (15, 80, 42, 5, 99, 23)
print("Maximum value:", max(my_tuple))
print("Minimum value:", min(my_tuple))'''

# 14. Write a program to calculate the sum of numeric elements in a tuple.
'''my_tuple = (10, 20, 30, 40, 50)
print("Sum of elements:", sum(my_tuple))'''

# 15. Write a program to sort a tuple of numbers in ascending order.
'''my_tuple = (40, 10, 50, 20, 30)
sorted_tuple = tuple(sorted(my_tuple))
print("Sorted Tuple (Ascending):", sorted_tuple)'''

# 16. Write a program to sort a tuple of strings alphabetically.
'''words_tuple = ("banana", "apple", "cherry", "date")
sorted_words = tuple(sorted(words_tuple))
print("Sorted Strings:", sorted_words)'''

# 17. Write a program to reverse a tuple.
'''my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = my_tuple[::-1]
print("Reversed Tuple:", reversed_tuple)'''

# 18. Write a program to check if two tuples are equal.
'''tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
if tuple1 == tuple2:
    print("Tuples are equal")
else:
    print("Tuples are not equal")'''

# 19. Write a program to remove duplicate elements from a tuple.
'''my_tuple = (1, 2, 2, 3, 4, 4, 5)
unique_tuple = tuple(dict.fromkeys(my_tuple))
print("Tuple without duplicates:", unique_tuple)'''

# 20. Write a program to find the length of the longest word in a tuple.
'''words_tuple = ("apple", "banana", "watermelon", "cherry")
longest_len = max(len(word) for word in words_tuple)
print("Length of the longest word:", longest_len)'''

# 21. Write a program to create a nested tuple and access its elements.
'''nested_tuple = ((1, 2, 3), ("a", "b", "c"))
print("Nested Tuple:", nested_tuple)
print("Element at [1][0]:", nested_tuple[1][0])'''

# 22. Write a program to flatten a nested tuple.
'''nested_tuple = ((1, 2), (3, 4), (5, 6))
flattened = tuple(item for subtuple in nested_tuple for item in subtuple)
print("Flattened Tuple:", flattened)'''

# 23. Write a program to swap two tuples.
'''tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple1, tuple2 = tuple2, tuple1
print("Tuple 1 after swap:", tuple1)
print("Tuple 2 after swap:", tuple2)'''

# 24. Write a program to find common elements between two tuples.
'''tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
common_elements = tuple(set(tuple1) & set(tuple2))
print("Common elements:", common_elements)'''

# 25. Write a program to find the difference between two tuples.
'''tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6)
diff = tuple(set(tuple1) - set(tuple2))
print("Elements in tuple1 but not in tuple2:", diff)'''

# 26. Write a program to convert a tuple of tuples into a dictionary.
'''tuple_of_tuples = (("a", 1), ("b", 2), ("c", 3))
result_dict = dict(tuple_of_tuples)
print("Converted Dictionary:", result_dict)'''

# 27. Write a program to unzip a list of tuples into individual lists.
'''list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*list_of_tuples)
print("List 1:", list(list1))
print("List 2:", list(list2))'''

# 28. Write a program to find repeated items in a tuple.
'''my_tuple = (1, 2, 3, 2, 4, 5, 1, 6)
repeated = tuple(set([x for x in my_tuple if my_tuple.count(x) > 1]))
print("Repeated items:", repeated)'''

# 29. Write a program to check if all elements in a tuple are the same.
'''my_tuple = (5, 5, 5, 5)
all_same = len(set(my_tuple)) == 1
print("Are all elements same?:", all_same)'''

# 30. Write a program to find the element-wise sum of two tuples.
'''tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
elementwise_sum = tuple(a + b for a, b in zip(tuple1, tuple2))
print("Element-wise sum:", elementwise_sum)'''
