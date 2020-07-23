

a = 5
b = 3
l = [[0] * b for i in range(a)]


#reverse a string
s[::-1]
[len(s)::-1]
s = ''.join(reversed(s))

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 


len(n)/2 returns 3.0
return -1
xrange(1, 4)


l = [1, 2, 3, 1]
for i in l:
    print(l.index(i))

range(1, 5)


a = [[1, 22], [2, 3], [3, 4]]
a.sort(key=lambda r: r[1])
vertices = set(list(i[0] for i in w_list))

dict.keys()




l = [1, 2, 3]
>>> print(' '.join(str(x) for x in l))
1 2 3
>>> print(' '.join(map(str, l)))
1 2 3


a = [1, 2, 3, 4, 5]
print(*a, sep = ',')



