import re
import read
import operator


df = read.load_data()

words = []

for line in df['headline']:
    for word in str(line).split():
        words.append(word.lower())
        
cleaned = [re.sub('[^a-zA-Z]+', '', word) for word in words]
        
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
        
results = sorted(counts.items(), 
                 key = operator.itemgetter(1))

results.reverse()

print(results[:101])