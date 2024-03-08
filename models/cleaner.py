import sys

with open(sys.path[0] + "/words.txt", "r") as f:
    content = f.readlines()

clean = set()

for item in content:
    item = item.strip()

    if item != "":
        clean.add(item)

clean=sorted(list(clean))

with open(sys.path[0] + "/fa_verbs.txt", "w") as f:
    f.writelines("\n".join(clean))
