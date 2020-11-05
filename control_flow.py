p = True
q = False

r = bool('true')
print(r)
print(type(r))

s = p and q
t = p and not q
u = p or q
v = (p or q) and p
print(v)

def add(i, b):
    print('in add i=' + str(i))
    return i + b


print()

u = False
#i = 50
if u:
    #print('i=' + str(i))
    print('u is true')
    print('u is still true')
else:
    i = 25
    print('u is not true')

print('after if block')
print('i=' + str(i))

print()

for i in range(4, 9):
    print('i=' + str(i))

print()
print(add(9, 5))
print()

print('i=' + str(i))
