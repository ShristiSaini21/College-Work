# 1. Write a Python program to create and display a set.
'''my_set = {10, 20, 30, 40, 50}
print("Set elements:", my_set)'''

# 2. Write a program to create a set with different data types.
'''mixed_set = {1, "Hello", 3.14, True}
print("Mixed data type set:", mixed_set)'''

# 3. Write a program to add a single element to a set.
'''my_set = {1, 2, 3}
my_set.add(4)
print("After adding 4:", my_set)'''

# 4. Write a program to add multiple elements to a set.
'''my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print("After adding multiple elements:", my_set)'''

# 5. Write a program to remove an element from a set using remove().
'''my_set = {10, 20, 30, 40}
my_set.remove(30)
print("After removing 30:", my_set)'''

# 6. Write a program to remove an element from a set using discard().
'''my_set = {10, 20, 30, 40}
my_set.discard(20)
print("After discarding 20:", my_set)'''

# 7. Write a program to clear all elements from a set.
'''my_set = {10, 20, 30}
my_set.clear()
print("After clearing set:", my_set)'''

# 8. Write a program to check if an element exists in a set.
'''my_set = {10, 20, 30, 40}
element = 30
if element in my_set:
    print(f"{element} exists in the set.")
else:
    print(f"{element} does not exist in the set.")'''

# 9. Write a program to find the length of a set.
'''my_set = {10, 20, 30, 40, 50}
print("Length of set:", len(my_set))'''

# 10. Write a program to iterate through a set and print its elements.
'''my_set = {10, 20, 30, 40}
print("Iterating through set:")
for item in my_set:
    print(item)'''

# 11. Write a program to find the union of two sets.
'''set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)'''

# 12. Write a program to find the intersection of two sets.
'''set1 = {1, 2, 3}
set2 = {2, 3, 4}
print("Intersection:", set1 & set2)'''

# 13. Write a program to find the difference of two sets.
'''set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Difference (set1 - set2):", set1 - set2)'''

# 14. Write a program to find the symmetric difference of two sets.
'''set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Symmetric Difference:", set1 ^ set2)'''

# 15. Write a program to check if a set is a subset of another set.
'''set1 = {1, 2}
set2 = {1, 2, 3, 4}
print("Is set1 a subset of set2?:", set1.issubset(set2))'''

# 16. Write a program to check if a set is a superset of another set.
'''set1 = {1, 2, 3, 4}
set2 = {1, 2}
print("Is set1 a superset of set2?:", set1.issuperset(set2))'''

# 17. Write a program to check if two sets are disjoint.
'''set1 = {1, 2}
set2 = {3, 4}
print("Are sets disjoint?:", set1.isdisjoint(set2))'''

# 18. Write a program to remove all elements of one set from another set.
'''set1 = {1, 2, 3, 4, 5}
set2 = {4, 5}
set1.difference_update(set2)
print("Set1 after removing elements of set2:", set1)'''

# 19. Write a program to create the power set of a given set.
'''from itertools import chain, combinations

def power_set(s):
    s_list = list(s)
    return list(chain.from_iterable(combinations(s_list, r) for r in range(len(s_list)+1)))

my_set = {1, 2}
print("Power Set:", power_set(my_set))'''

# 20. Write a program to find the Cartesian product of two sets.
'''from itertools import product

set1 = {1, 2}
set2 = {'a', 'b'}
cartesian_prod = list(product(set1, set2))
print("Cartesian Product:", cartesian_prod)'''

# 21. Write a program to count distinct elements from a list using a set.
'''my_list = [1, 2, 2, 3, 4, 4, 5]
distinct_count = len(set(my_list))
print("Number of distinct elements:", distinct_count)'''

# 22. Write a program to find duplicate elements in a list using a set.
'''my_list = [1, 2, 3, 2, 4, 5, 1]
seen = set()
duplicates = set(x for x in my_list if x in seen or (seen.add(x) is None and False)) # alternative logic below
# Simpler approach for duplicates:
duplicates = set([x for x in my_list if my_list.count(x) > 1])
print("Duplicate elements:", duplicates)'''

# 23. Write a program to remove duplicates from a list using a set.
'''my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print("List without duplicates:", unique_list)'''

# 24. Write a program to convert a string into a set of characters.
'''my_string = "programming"
char_set = set(my_string)
print("Set of characters:", char_set)'''

# 25. Write a program to find common letters in two strings using sets.
'''str1 = "apple"
str2 = "peach"
common_letters = set(str1) & set(str2)
print("Common letters:", common_letters)'''

# 26. Write a program to find unique words in a sentence using a set.
'''sentence = "python is great and python is easy"
words = set(sentence.split())
print("Unique words:", words)'''

# 27. Write a program to check if two strings are anagrams using sets.
'''str1 = "listen"
str2 = "silent"
is_anagram = set(str1) == set(str2) and len(str1) == len(str2)
print("Are strings anagrams?:", is_anagram)'''

# 28. Write a program to create a frozen set and demonstrate its properties.
'''my_frozen = frozenset([1, 2, 3, 4])
print("Frozen Set:", my_frozen)
# my_frozen.add(5) # Error: frozenset is immutable'''

# 29. Write a program to find maximum and minimum values in a set.
'''my_set = {15, 80, 42, 5, 99}
print("Maximum value:", max(my_set))
print("Minimum value:", min(my_set))'''

# 30. Write a program to perform all basic set operations (union, intersection, difference, symmetric difference) in one program.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)
