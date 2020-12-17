class MyException(Exception):
    pass

try:
    a = int(input('Give me a: '))
    # a = 4
    import sys

    sys.stderr.write('Im writing to error stream\n')
    b = 20
    c = a + b
    #c = a * d
    if c > 25:
        raise MyException('- error: a+b>25')
    print(c)
    #print(c)
except (NameError, ValueError) as nve:
    print(type(nve))
    print('ValueError or NameError handling: ' + str(nve))
except Exception as e:
    print(type(e))
    print(str(e))

print('continuing....')
