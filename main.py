## Program to solve a word search puzzle

## Inputting words list
words =[]
len = int(input("How many words would you like to search? :"))
for i in range(len):
    word = input(f"Please enter word {i+1}:")
    words.append(word)

# Reading word matrix

fobj = open("matrix.txt",'r')

matrix = []

for line in fobj.readlines():
    matrix.append(line.split())
# print(matrix)