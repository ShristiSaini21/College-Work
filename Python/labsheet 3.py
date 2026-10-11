#check if a string is palindrome
'''text= input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")'''

#vowel or consonant in a string
'''text = input("Enter a string: ")
vowels = consonants = 0

for char in text.lower():
    if char.isalpha():
        if char in "aeiou":
         vowels += 1
    else:
         consonants +=1
print(f"Vowels:{vowels}, Consonants: {consonants}")'''

#replace all spaces in a string with underscores
'''text = input("Enter a string: ")
result = text.replace(" ", "_")
print("Modified string:", result)'''

#uppercase character from a string
'''text = input("Enter a string: ")
uppercase_chars = [char for char in text if char.isupper()]
print("Uppercase characters:", "".join(uppercase_chars))'''

#remove duplicate character from a string
'''text = input("Enter a string: ")
result = ""
for char in text:
    if char not in result:
        result += char
print("String without duplicates:", result)'''

#find frequency from a string
'''text = input("Enter a string: ")
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

for char, count in freq.items():
    print(f"'{char}': {count}")'''

#reverse string without using slicing
'''text = input("Enter a string: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed string:", reversed_text)'''

#convert a string into title case without using built-in functions
'''text = input("Enter a string: ")
result = []
capitalize_next = True

for char in text:
    if char.isspace():
        result.append(char)
        capitalize_next = True
    elif capitalize_next:
        result.append(char.upper())
        capitalize_next = False
    else:
        result.append(char.lower())

print("Title case:", "".join(result))'''

#count the number of words in a string
'''text = input("Enter a string: ")
words = text.split()
print("Number of words:", len(words))'''

#find the longest word in a string
'''text = input("Enter a string: ")
words = text.split()
longest_word = max(words, key=len) if words else ""
print("Longest word:", longest_word)'''

#two strings are anagrams of each other
'''str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", "")):
    print("Anagrams")
else:
    print("Not anagrams")'''

#substring exists in a string
'''text = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in text:
    print("Substring exists.")
else:
    print("Substring does not exist.")'''

#convert all vowels in a string to uppercase and consonants to lowercase
'''text = input("Enter a string: ")
result = []

for char in text:
    if char.lower() in "aeiou":
        result.append(char.upper())
    elif char.isalpha():
        result.append(char.lower())
    else:
        result.append(char)

print("Converted string:", "".join(result))'''

#remove all punctuation from a string
'''import string

text = input("Enter a string: ")
no_punct = "".join(char for char in text if char not in string.punctuation)
print("String without punctuation:", no_punct)'''

#first non-repeated character in a string
'''text = input("Enter a string: ")
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

for char in text:
    if freq[char] == 1:
        print("First non-repeated character:", char)
        break
else:
    print("No non-repeated character found.")'''

#count the number of digits, alphabets, and special characters in a string
'''text = input("Enter a string: ")
digits = alphabets = special = 0

for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        alphabets += 1
    else:
        special += 1

print(f"Alphabets: {alphabets}, Digits: {digits}, Special Characters: {special}")'''

#print all substring of a string
'''text = input("Enter a string: ")
print("All substrings:")
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        print(text[i:j])'''

#sort the characters of a string alphabetically
'''text = input("Enter a string: ")
sorted_text = "".join(sorted(text))
print("Sorted string:", sorted_text)'''

#most repeated word in a string
'''text = input("Enter a string: ")
words = text.lower().split()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

if word_counts:
    most_repeated = max(word_counts, key=word_counts.get)
    print(f"Most repeated word: '{most_repeated}' ({word_counts[most_repeated]} times)")'''

#two strings are rotations of each other
'''str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Rotations of each other")
else:
    print("Not rotations of each other")'''

#find the largest and smallest elements in a list
'''nums = [int(x) for x in input("Enter space-separated numbers: ").split()]

if nums:
    print("Largest:", max(nums))
    print("Smallest:", min(nums))'''

#sort a list of integers in ascending and descending order
'''nums = [int(x) for x in input("Enter space-separated numbers: ").split()]

print("Ascending order:", sorted(nums))
print("Descending order:", sorted(nums, reverse=True))'''

#remove duplicate elements from a list
'''nums = [int(x) for x in input("Enter space-separated numbers: ").split()]
unique_nums = list(dict.fromkeys(nums))
print("List without duplicates:", unique_nums)'''

#remove a list without using built-in functions
'''lst = input("Enter space-separated elements: ").split()
reversed_lst = []

for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])

print("Reversed list:", reversed_lst)'''

#count the frequency of each the element in a list
'''lst = input("Enter space-separated elements: ").split()
freq = {}

for item in lst:
    freq[item] = freq.get(item, 0) + 1

for item, count in freq.items():
    print(f"'{item}': {count}")'''

#merge two lists into one
'''list1 = input("Enter first list elements: ").split()
list2 = input("Enter second list elements: ").split()

merged_list = list1 + list2
print("Merged list:", merged_list)'''

#find the second largest number in a list
'''nums = list(set(int(x) for x in input("Enter space-separated numbers: ").split()))

if len(nums) < 2:
    print("List must contain at least two distinct numbers.")
else:
    nums.sort()
    print("Second largest number:", nums[-2])'''

#find common elements is two lists
'''list1 = input("Enter first list elements: ").split()
list2 = input("Enter second list elements: ").split()

common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)'''

#find the difference b/w two lists
'''list1 = input("Enter first list elements: ").split()
list2 = input("Enter second list elements: ").split()

diff = [item for item in list1 if item not in list2]
print("Difference (List1 - List2):", diff)'''

#separate even or odd numbers from a list
'''nums = [int(x) for x in input("Enter space-separated numbers: ").split()]

evens = [x for x in nums if x % 2 == 0]
odds = [x for x in nums if x % 2 != 0]

print("Even numbers:", evens)
print("Odd numbers:", odds)'''

