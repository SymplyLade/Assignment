# Unique Name Collector 
names =set()
while True:
    name = input("Enter a name (or 'done' to finish):")
    if name.lower() == "done":
        break
    names.add(name)
    for name in sorted(names):
        print(name)