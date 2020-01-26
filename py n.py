#this doc writes python lines

#!/usr/bin/env python
# coding: utf-8

###################################################################
#todo
ord()



###################################################################
#class

_var intended private
var_ avoid collision
__var avoid subclass name collision
__var__ python use



###################################################################
# function
def __init__( self ):


def returntuple():
    a = 4
    b = 5
    c = 8
    return a, b, c
print(returntuple())
#(a, b, c)


###################################################################
#datatypes
#list
.list()
#convert to list

list.pop()
#get the last one; remove it from the list

list.index(item)
#return index

set()
range()

res = [None] * size #create an empty [] of len(size)



###################################################################
#syntax
x = 1 if 2>1 else 0
x = x for x in y if x > 0


assert item in self._theItems, "The item must be in the bag."



###################################################################
#common funcs
print()
dir(instance)
# print all attributes' names




###################################################################
#libs
random
array

ctypes
from array import Array








###################################################################
else




x = 1 if 2>1 else 0
x = x for x in y if x > 0



a = ["1","2","5"]
n1 = ord(a.pop())-ord('0')

for i in range(5):
    print(i)
# 0 1 2 3 4


#input domain, extreme cases

# basic operation
get_ipython().run_line_magic('', '')


k = None
if not k:
    print('rua')
if k is None:
    print('rua')


k = 0
if not k:
    print('rua')


if k is None:



def g(y):

	print(x)
	print(x + 1)
x = 5
g(x)
print(x)

def h(y):
	print(x)
	x = x +1
x=5
h(x)
print(x)

a = (1,2,3)
for i in a:
	print(i)

a = 0
L = [1,2,3,4,5]
for i in range(len(L)):
	print(L[i])
	a += L[i]
print(a)

a = ['red', 'yellow', 'orange']
print(a)
# ba = sorted(a)
b = a.sorted()
print(b)
print(sa)
print(ba)

b = ['grey', 'green', 'blue']
sb = sorted(b)
print(b)
print(sb)

a = [3,4,1]
c = a.sort()
c = sorted(a)

print(a)
print(c)
# print(c)
print(a)


def mult(a, b):
	result = 0
	while b > 0:
		result += a
		b -= 1

	return result

x = mult(1,2)
print(x)

a = [1,2]
b = (1,2)
c = '123'
if '12' in c:
	print( 'true' )

d = (1, (2,3))
print(d)

a = [1,2,3]
if b is not None:
	print('None')




















