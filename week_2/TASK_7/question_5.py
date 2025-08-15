# Contact Quick Lookup
names = ('Lade', 'Malik', 'Ade')
phone_nos = ('903326', '0705946', '806041')
info = {name: num for name, num in zip(names, phone_nos)}
new_name = input('Enter a name: ')
print(info.get(new_name))