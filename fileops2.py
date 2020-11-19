import os

dir = 'c:\\dev\\Python_Winter_2020_2'

file = 't.txt'

myfile = os.path.join(dir, file)
print(myfile)
print(os.path.exists(myfile))
print(os.path.isfile(myfile))
print(os.path.isdir(myfile))


print('Current working dir: ' + os.getcwd())
#os.mkdir('mydir')
#os.rmdir('mydir')


print(os.getenv('PATH'))
