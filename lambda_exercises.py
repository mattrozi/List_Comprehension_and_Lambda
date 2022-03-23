""" 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
"""

from calendar import weekday


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda x: x % 2 == 0, original_list))
# print(even_list)

odd_list = list(filter(lambda x: x % 2 == 1, original_list))
# print(odd_list)


""" 2)
find which days of the week have exactly 6 characters.
"""

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

six_chars = list(filter(lambda x: (len(x) == 6), weekdays))
print(six_chars)


""" 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

"""

colors = ["orange", "red", "green", "blue", "white", "black"]
filtered_list1 = list(filter(lambda x: ("a" not in x), colors))
print(filtered_list1)


""" 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 """
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

list3 = list(filter(lambda x: x not in list2, list1))
print(list3)

""" 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

"""

colored_list = ["red", "black", "white", "green", "orange"]
substring1 = list(filter(lambda x: "ack" in x, colored_list))
print(substring1)

substring2 = list(filter(lambda x: "abc" in x, colored_list))
print(substring2)


""" 6)
check whether a given string contains a capital letter, a lower case letter, 
a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
"""
password = "Lak3rsya"
checks = [
    lambda x: any(x.lower() in password),
    lambda x: any(x.upper() in password),
    lambda x: any(x.isalpha() in password),
    lambda x: any(len(x) >= 8 in password),
]

checked_password = list(filter(checks, password))
print(checked_password)

""" 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
