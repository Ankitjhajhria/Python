#this program is for reading lines form python

#this code will make us read a single line
file_main = open("a.txt",'rt')
print File_main

#this is with .read function
file_main = open ("a.txt", 'rt')
read_file = file_main.read()
print type(read_file)

#this is with .readline and will read all lines toghter
file_main = open ("a.txt", 'rt')
read_file = file_main.readline()
print read_file

#this is for reading all lines 
read_file = file_main.readlines()
print type(read_file)

#this is for looping to read all lins of file

for i in  file_main:
    print i


