import os
from random import sample
from nltk import tokenize

print("type the name of the file you wish to split by new lines into multiple files")
fileName = input()
print("enter the number of sentences you want")
num = int(input())

file = open(fileName)
lines = file.readlines()
lines = [l for l in lines if len(tokenize.word_tokenize(l)) > 10]
lines = sample(lines, num)
i = 0
os.mkdir(fileName[:-4])
while i < num:
    directory = fileName[:-4] + "/" + str(i) + ".txt"
    current_file = open(directory, 'w')
    current_file.write(lines[i])
    i += 1
