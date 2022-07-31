## Program to solve a word search puzzle

## Inputting words list
words =[]

for i in int(input("How many words would you like to search? :")):
    word = input(f"Please enter word {i}:")
    words.append(word)

# Reading word matrix

fobj = open("matrix.txt",'r')

matrix = []

for line in fobj.readlines():
    matrix.append(line.split())
# print(matrix)