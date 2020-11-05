a = 50
a
50
type(a)
#<class 'int'>
a = 'abc'
type(a)

#<class 'str'>

i = 5
#print('i=' + str(i))
print('i={0}'.format(i))

#j = 0.0000000000000000000007597245987259827597259672672067230697329
j = 6326362362363263636367597245987259827597259672672067230697329
k = j+2
print(j)
print(k)
print(type(k))


print()
a = 'abcdef'

pos_cd = a.index('cd')
print(pos_cd)

def index(stack, needle):
    return stack.index(needle)

print(index(a, 'cd'))

print()
print(a)
#b = a[2:]
#b = a[:2]
#b = a[2:4]
b = a[-3:]
print(b)