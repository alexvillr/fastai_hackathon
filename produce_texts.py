# informal text
# https://www.reddit.com/r/funny/comments/vmvbil/beats_most_fashion_walks/
#
# formal text
# https://en.wikipedia.org/wiki/Operation_Scorched_Earth
import re


informal = open("informal.txt").read()
formal = open("formal.txt").read()

split_informal = re.split(".\n", informal)
informal_dataset = []

for sentence in split_informal:
    if 10<= len(sentence.split()):
        informal_dataset.append(sentence)

split_formal = re.split(".\n", formal)
formal_dataset = []

for sentence in split_formal:
    if 10 <= len(sentence.split()):
        formal_dataset.append(sentence)

print("Formal Data")
print(formal_dataset)
print("Informal Data")
print(informal_dataset)