#!/usr/bin/python3

hi_list = ' '
for i in range(10):
  hi_list += '5'
  print(' '.join(hi_list))
  
print()
 
hi_list = []
for i in range(10):
  hi_list += ['Best School']
  print(' '.join(hi_list))
  
print()  
for x in range(5):
  for y in range(5):
    print(y, end=' ')
  print()

print()  
for x in range(5):
  for y in range(x+1):
    print(y, end=' ')
  print()  

print()  
for x in range(65, 70):
  for y in range(65, 70):
    print(y, end=' ')
  print()

print()  
for x in range(65, 70):
  for y in range(65, 70):
    print(chr(y), end=' ')
  print()
  
print()
for x in range(65, 70):
  for y in range(65, x+1):
    print(chr(y), end=" ")
  print ()

print()
for x in range(65, 70):
  for y in range(65, 70):
    temp = []
    temp.append('X')
    print(' '.join(temp), end=" ")
  print()

print()
List_of_st = 0
for i in range(5):
  List_of_st += i
  print(List_of_st, end=' ')

print()
