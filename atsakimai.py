# # 1 uzduotis
# def find_longest_word(filename):
#     longest_word = ""
#     with open(filename, "r", encoding="UTF-8") as file:
#         for line in file:
#             word = line.strip()
#             if len(word) > len(longest_word):
#                 longest_word = word
#     return longest_word
# filename = "words.txt"
# longest_word = find_longest_word(filename)
# print("Longest Word:", longest_word)
# print("Length:", len(longest_word))
# 2 uzduotis
# def is_palindrome(string):
#     lowercase_string = string.lower()
#     alphanumeric_chars = [char for char in lowercase_string if char.isalnum()]
#     reversed_chars = alphanumeric_chars[::-1]
#     return alphanumeric_chars == reversed_chars
# strings = ["level", "python", "Madam", "12321", "racecar"]
# for string in strings:
#     print("String:", string)
#     if is_palindrome(string):
#         print("Palindrome: Yes")
#     else:
#         print("Palindrome: No")
# # 3 uzduotis
from functools import reduce
def calculate_product(numbers):
    product = reduce(lambda x, y: x * y,
                     [num for num in numbers if num % 2 == 0])
    return product
def calculate_squares(numbers):
    squares = [num**2 for num in numbers if num % 2 != 0]
    return squares
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = calculate_product(numbers)
squares = calculate_squares(numbers)
print("Product of even numbers:", product)
print("Squares of odd numbers:", squares)
# # 4 uzduotis
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# year = int(input("Enter a year: "))
# if is_leap_year(year):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")
# # 5 uzduotis
# def division(a, b):
#     result = 0
#     try:
#         result = a / b
#         return result
#     except:
#         print("Negalima dalyba iš 0")
#         return None
# while True:
#     try:
#         a = int(input("Input the first number: "))
#         b = int(input("Input the second number: "))
#         result = division(a, b)
#         if result:
#             print("Division successful. Result is:", result)
#         break
#     except ValueError:
#         print("Please input an integer number")
#         continue