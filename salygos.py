# my_list = []
#
# for i in range(1, 10001):
#     if i % 6 == 0:
#         my_list.append(i)
# print(my_list)
# # #
# # my_list = []
# for i in range(10000):
#     if '9' in str(i):
#         my_list.append(i)
# print(my_list)
# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# number_of_words = 0
# text = text.split()
# for word in text:
#     if len(word) > 5:
#         number_of_words +=1
# print(number_of_words)




def calkulatorius(a,b):
    print(a +b)
    print(a - b)
    print(a * b)
    print(a / b)

first = int(input('Type first number: '))
second = int(input('Type second number: '))
calkulatorius(first, second)
