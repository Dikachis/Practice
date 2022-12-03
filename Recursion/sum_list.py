#!/usr/bin/python3
print("Function that sum two value arg values")
def sum(a, b):
    y = a + b
    print(y)

sum(8, 10)

print("Function that sum up the values (len(arg_val)) in the my_list")
def add(my_list):
    sum = 0
    for num in my_list:
        sum += num
    print(sum)

add([3, 4, 5, 1, 10])

print("Function that sum up the values (len(arg_val)) in the tuple(*args)")
def add(*args):
    sum = 0
    for num in args:
        sum += num
    print(sum)

add(3, 4, 5, 5, 10)

print("Function that prints dictionary (**kwargs) or the key and value of python dictionarys")
def my_func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_func(a='hello', b=10)
my_func(param1=True, param2=10.5)