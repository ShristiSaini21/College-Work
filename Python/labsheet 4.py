#find the sum and average of elements in a list
'''lst = [10, 20, 30, 40, 50]
total_sum = sum(lst)
average = total_sum / len(lst) if lst else 0
print(f"Sum: {total_sum}, Average: {average}")'''

#rotate a list by n positions
'''lst = [1, 2, 3, 4, 5]
n = 2
n = n % len(lst)
rotated_lst = lst[-n:] + lst[:-n]
print("Rotated List:", rotated_lst)'''

#remove all negative numbers from a list
'''lst = [12, -3, 45, -6, 0, -8, 9]
positive_lst = [x for x in lst if x >= 0]
print("List after removing negatives:", positive_lst)'''

#remove all negative numbers from a list
'''lst = [12, -3, 45, -6, 0, -8, 9]
positive_lst = [x for x in lst if x >= 0]
print("List after removing negatives:", positive_lst)'''

#find the product of all elements in a list
'''import math
lst = [2, 3, 4, 5]
product = math.prod(lst)
print("Product of all elements:", product)'''

#create a list of square of numbers from 1 to n
'''n = 5
squares = [i**2 for i in range(1, n + 1)]
print("Squares list:", squares)'''

#split a list into two halves
'''lst = [10, 20, 30, 40, 50, 60]
mid = len(lst) // 2
print("First half:", lst[:mid])
print("Second half:", lst[mid:])'''

#check if a list is sorted or not
'''lst = [1, 3, 5, 7, 9]
if lst == sorted(lst) or lst == sorted(lst, reverse=True):
    print("The list is sorted.")
else:
    print("The list is not sorted.")'''

#find pairs of numbers in a list whose sum is equal to a given number
'''lst = [2, 4, 3, 5, 7, 8, -1]
target = 7
pairs = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i], lst[j]))
print("Pairs with given sum:", pairs)'''

#flatten a nested list
'''nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened)'''

#convert a list into a string without using join()
'''lst = ['H', 'e', 'l', 'l', 'o']
result_str = ""
for char in lst:
    result_str += str(char)
print("Converted String:", result_str)'''

#create a dictionary of student names and marks and display it
'''student_dict = {'Aman': 85, 'Rahul': 90, 'Priya': 95}
print("Student Dictionary:", student_dict)'''

#find the maximum and minimum marks from a dictionary
'''student_dict = {'Aman': 85, 'Rahul': 92, 'Priya': 78}
max_student = max(student_dict, key=student_dict.get)
min_student = min(student_dict, key=student_dict.get)
print(f"Max marks: {student_dict[max_student]} by {max_student}")
print(f"Min marks: {student_dict[min_student]} by {min_student}")'''

#count the frequency of characters in a string using a dictionary
'''s = "programming"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print("Character frequency:", freq)'''

#merge two dictionaries into one
'''dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)'''

#sort a dictionary by keys
'''d = {'banana': 3, 'apple': 1, 'cherry': 2}
sorted_by_keys = dict(sorted(d.items()))
print("Sorted by keys:", sorted_by_keys)'''

#sort a dictionary by values
'''d = {'banana': 3, 'apple': 1, 'cherry': 2}
sorted_by_values = dict(sorted(d.items(), key=lambda item: item[1]))
print("Sorted by values:", sorted_by_values)'''

#update the value of a key in a dictionary
'''d = {'a': 10, 'b': 20}
d['a'] = 50
print("Updated dictionary:", d)'''

#remove a key from a dictionary
'''d = {'a': 10, 'b': 20, 'c': 30}
d.pop('b', None)
print("Dictionary after removal:", d)'''

#check if a key exists in a dictionary
'''d = {'a': 10, 'b': 20}
key = 'a'
if key in d:
    print("Key exists!")
else:
    print("Key does not exist.")'''

#find the sum of all values in a dictionary
'''d = {'a': 10, 'b': 20, 'c': 30}
total_sum = sum(d.values())
print("Sum of all values:", total_sum)'''

#find the key with the maximum value in a dictionary
'''d = {'math': 85, 'science': 95, 'english': 90}
max_key = max(d, key=d.get)
print("Key with max value:", max_key)'''

#create a dictionary with numbers as keys and their squares as values
'''n = 4
square_dict = {i: i**2 for i in range(1, n + 1)}
print("Dictionary of squares:", square_dict)'''

#convert two lists into a dictionary
'''keys = ['name', 'age', 'city']
values = ['Rahul', 21, 'Delhi']
combined_dict = dict(zip(keys, values))
print("Combined dictionary:", combined_dict)'''

#invert a dictionary
'''d = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {v: k for k, v in d.items()}
print("Inverted dictionary:", inverted_dict)'''

#count word frequency in a given paragraph using a dictionary
'''paragraph = "apple banana apple orange banana apple"
words = paragraph.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word frequency:", word_freq)'''

#check if two dictionaries are equal
'''d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}
if d1 == d2:
    print("Dictionaries are equal.")
else:
    print("Dictionaries are not equal.")'''

#remove duplicate values from a dictionary
'''d = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
seen_values = set()
unique_dict = {}
for k, v in d.items():
    if v not in seen_values:
        seen_values.add(v)
        unique_dict[k] = v
print("Dictionary after removing duplicate values:", unique_dict)'''

#create a nested dictionary for student details (Name, Roll, Marks)
'''students = {
    'student1': {'Name': 'Aman', 'Roll': 101, 'Marks': 88},
    'student2': {'Name': 'Neha', 'Roll': 102, 'Marks': 92}
}
print("Nested Dictionary:", students)'''

#find common keys between two dictionaries
'''d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 20, 'c': 30, 'd': 40}
common_keys = set(d1.keys()).intersection(set(d2.keys()))
print("Common keys:", common_keys)'''

#create a dictionary from a string with characters as keys and frequency as values
s = "hello"
char_dict = {char: s.count(char) for char in set(s)}
print("Character frequency dictionary:", char_dict)
