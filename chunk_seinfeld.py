import pandas as pd
import re
from nltk import tokenize
seinfeld = pd.read_csv("seinfeld.csv")

sentences = tokenize.sent_tokenize(re.sub(r'\(.*?\) *', '', ' '.join([str(x) for x in seinfeld["Dialogue"].tolist()])))

file = open("seinfeld.txt", 'w')
file.write('\n'.join(sentences))
file.close()
