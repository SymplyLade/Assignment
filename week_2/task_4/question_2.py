# Shopping List Manager
shopping_list = []
for i in range(3):
    item = input(f"Enter shopping item{i+1}:")
shopping_list.append(item)
print(", ".join(shopping_list))