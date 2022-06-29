import os

print("type the name of the file you wish to split by new lines into multiple files")
fileName = input()

file = open(fileName)
i = 0
os.mkdir(fileName[:-4])
while i <= 200:
    directory = fileName[:-4] + "/" + str(i) + ".txt"
    current_file = open(directory, 'w')
    current_file.write(file.readline())
    i += 1