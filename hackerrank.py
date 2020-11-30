# Problem: find runner up
# n = int(input())
# arr = list(map(int, input().split()))[:n]
# champion = max(arr)
# runner_up = max(arr, key=lambda x: min(arr) - 1 if (x == champion) else x)
# print(runner_up)

# Problem: Finding the percentage
# n = int(input())
# student_marks = {}
# for i in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# for key, value in student_marks.items():
#     if query_name == key:
#         average = sum(value) / len(value)
#         print("{:0.2f}".format(average))


# Problem: What's Your Name?
# firstname = input()
# lastname = input()
#
#
# def print_full_name(firstname, lastname):
#     print("Hello {} {}! You just delved into python.".format(firstname, lastname))


# Problem: Capitalize!
# fullname = input()
# print(fullname.title())

# dec = 10
# print(dec, oct(dec), hex(dec), bin(dec))

# Problem: Tuples
# n = int(input())
# integer_list = tuple(map(int, input().split()))
#
# print(hash(integer_list))

# Problem: Nested Lists
# n = int(input())
# final_list = []
# for i in range(n):
#     name = input()
#     score = float(input())
#     temp_list = [name, score]
#     final_list.append(temp_list)
#     print(final_list)
# for i in range(n):
#     print(final_list[i][1])

# Problem: sWAP cASE
# def swap_case(s):
#     return s.swapcase()
#
#
# s = input()
# result = swap_case(s)
# print(result)

# Problem: String Split and Join
# s = input()
# s = s.split(" ")
# s = "-".join(s)

# Problem: Mutations
# def mutate_string(string, position, character):
#     l = list(string)
#     l[position] = character
#     string = ''.join(l)
#     return string
#
#
# s = input()
# i, c = input().split()
# s_new = mutate_string(s, int(i), c)
# print(s_new)

# Problem: Find a string
# def count_substring(string, sub_string):
#     count = 0
#     flag = True
#     start = 0
#     while flag:
#         a = string.find(sub_string, start)  # find() returns -1 if the word is not found,
#         # start i the starting index from the search starts(default value is 0)
#         if a == -1:  # if pattern not found set flag to False
#             flag = False
#         else:  # if word is found increase count and set starting index to a+1
#             count += 1
#             start = a + 1
#     return count
#
#
# string = input().strip()
# sub_string = input().strip()
#
# count = count_substring(string, sub_string)
# print(count)

# Problem: Text Wrap
# def wrap(string, max_width):
#     import textwrap
#     return textwrap.fill(string, max_width)
#
#
# string, max_width = input(), int(input())
# result = wrap(string, max_width)
# print(result)

# Problem: Capitalize
# def solve(s):
#     for x in s[:].split():
#         s = s.replace(x, x.capitalize())
#     return s
#
#
# s = input()
#
# result = solve(s)
# print(result)

# Problem: itertools.product()
# from itertools import product
#
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# print(*product(A, B))
# # C = [A, B]
# print(tuple(list(product(*C))))


# myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
# print(Counter(myList))
# Problem: collections.Counter()
from collections import Counter

# x = int(input())
# shoes = list(map(int, input().split()))[:x]
# n = int(input())
# for i in range(n):
#     size_price = list(map(int, input().split()))

# Problem: Set
# x = int(input())
# height = list(map(int, input().split()))[:x]
# height = set(height)
# print(sum(height) / len(height))


# Problem: itertools.permutations()
# from itertools import permutations
#
# data, size = map(str, input().split())
#
# permu = list(permutations(data, int(size)))
# permu.sort()
# for p in permu:
#     print(''.join(p))

# Problem: calendar
# import datetime
# import calendar
#
#
# def findDay(date):
#     born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
#     return (calendar.day_name[born]).upper()
#
#
# # Driver program
# mm, dd, Y = map(str, input().split())
# date = str(dd) + ' ' + str(mm) + ' ' + str(Y)
# print(findDay(date))

# Problem:
