import read

df = read.load_data()

top = df['url'].value_counts()

results = []

for name, count in top.items():
    results.append((name, count))
    
print(results[:101])