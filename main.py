# # Dictionary comprehensions
# Dictionaries also have this fancy one liner comprehension functionality:

# Let's say we have the same problem of perfect squares but we want to have number: 
# percect_square structure like this: {1: 1, 2: 4, 3: 9} Try writing this without dictionary comprehension yourself.

# Dictionary comprehension example:

# squares = {i: i * i for i in range(10)}
# print(squares)

# Try doing both exercises done with lists:

# program without perfect square of 5.
# only odd numbers.
# Enumerate
# Let's imagine we have a python loops over some items in the list:

# values = ["a", "b", "c"]

# for value in values:
#     print(value)
# it is a simple nice loop, that does all it has to. Now imagine you also want to get the corresponding index of the item. How would you do it?

# You could do something like this:

# values = ["a", "b", "c"]
# index = 0

# for value in values:
#     print(index, value)
#     index += 1
# So here we have an integer that increments with each iteration and it also works. 
# But too keep our code simpler we may use python build int function enumerate()

# values = ["a", "b", "c"]
# for count, value in enumerate(values):
#     print(count, value)
# If we wanted to change the start count:

# values = ["a", "b", "c"]
# for count, value in enumerate(values, start=1):
#     print(count, value)
# If we go a bit crazy we can combine two things we learned today:

# def even_items(numbers: list):
#     return [v for i, v in enumerate(numbers, start=1) if not i % 2]
# seq = list(range(1, 11))
# print(even_items(seq))

# Go through this once yourself, operate small things out and combine them together once again.

# NOTE enumerate returns an iterator so if you want to look what's inside you can either loop through it or convert it to list.

# # math library
# for many math specifics you can use math library in python. It is a built in library simply just:

# import math
# and you are good to go.
# For example if you wanted to calculate a circle area:

# import math
# area = 5 * 5 * math.pi
# math.pi 
# print(area)
# here is a constact which we can you straight out of the box.

# There are plenty more functions we could spend all day reviewing this library cause it's huge, but let's look into couple of more functions.

# factorial
# For example if we wanted to calculate factorial: 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
# We could write a function ourselves, but actually it is already available to us:

# import math
# math.factorial(7)
# What is more it is actually quite optimised as well.

# ceil() and floor()
# All there functions do is that if you have a float value, it can literaly get "floor" or "ceiling" of it. Examples:

# import math
# print(math.ceil(6.1))
# print(math.floor(-11.1))

# Is this clear?

# power functions
# Let's say you want to have a number raised by the power of n: 5^5 = 5 * 5 * 5 * 5 * 5 = 3125

# import math
# print(math.pow(5, 5))

#square root
# import math
# print (math.sqrt(9))

# There are many more things in math library as said before, here we reviewed just a tiny bit. 
# But bottom line is that if you ahve something to do with math, logarithms, working with angles, trigonometry etc.

# Exercises 🧠 :
# 3.
# Given string: text = 'In this lecture we will review some additional functionalities of python built-in data structures.' 
# calculate how many words have letter 'e' in it.

# text = "In this lecture we will review some additional functionalities of python built-in data structures."
# splited_text = ([words for words in text.split() if "e" in words])
# count = 0
# for word in splited_text:
#   if 'e' in word:
#     count += 1
# print(count)          

# 4. Given the same string as in previous exercise: calculate count of words that have more than 5 characters.

# text = "In this lecture we will review some additional functionalities of python built-in data structures."
# splited_text = ([words for words in text.split() if len(words) > 5])
# count = 0
# for word in splited_text:
#     if len(word) > 5:
#         count += 1
# print(count)

# 5. Given the same string calculate the occurrence of each letter in the string. (HINT: store everything in dictionary)
# text = "In this lecture we will review some additional functionalities of python built-in data structures."
# occurrence = {}
# for letter in text:
#   if letter.isalpha():
#     if letter in occurrence:
#         occurrence[letter] += 1
#     else:
#         occurrence[letter] = 1
# print(occurrence)
# for letter, count in occurrence.items():
#   print(f"{letter}: {count}")

# 5.1 pagal tema
text = 'In this lecture we will review some additional functionalities of Python built-in data structures.'
# text = text.replace(" ", "").lower()
occurrence = {letter: text.count(letter) for letter in text if letter.isalpha()}
print(occurrence)
for letter, frequency in occurrence.items():
    print(f"{letter}: {frequency}")


#   squares = {i: i * i for i in range(10)}
# print(squares)

# 6. Write a program that checks if given number is a perfect square.


