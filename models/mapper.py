import sys,re

with open(sys.path[0]+"/sample/fa_commands.txt","r") as f:
    content=f.readlines()

words=set()

for line in content:
    # Skip commands ro comments
    if line.startswith(("//","--")):
        continue

    # Tokenize
    line=re.sub(' +', ' ', line)
    line = line.split()


    # Filter
    line = [word for word in line if word not in ["رو", "را","بهم"]]


    # Find all words
    for w in line:
        words.add(w)


    if len(line)>0:
        print(line)


    # Visualize

print(words)


# print(content)