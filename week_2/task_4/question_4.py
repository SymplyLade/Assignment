# Name Organizer
names = input("Enter 5 names separated by spaces:").split()
names_lower = [name.lower() for name in names]
names_lower.sort()
for name in names_lower:
    print(name)