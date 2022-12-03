#!/usr/bin/python3

List_of_str = []
for i in range(10):
    List_of_str += ["BestSchool"]
    print(", ".join(List_of_str))

print()
List_of_str = [1, 3, 5, 2, 5]
List_of_st = 0
for i in List_of_str:
    List_of_st += i
    print(List_of_st)

print()
List_of_st = 0
for i in range(5):
    List_of_st += i
    print(List_of_st)
                      
print()
List_of_str = ['1', '3', '5', '2', '5']
List_of_st = 0
for i in range(5): # iterate the list (List_of_str) 5 times
    List_of_st += i
    print(", ".join(List_of_str))
