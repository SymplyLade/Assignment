# Tuple Unpacking
profile = ( 
input("Enter your first_name:"), 
int(input("Enter your age:")),
input("Enter Favorite color:"),
input("Enter your hometown:"))
# storing and unpacking them in variable
first_name, age, color,hometown = profile
print(f"{first_name} \n {age} \n {color} \n {hometown}")