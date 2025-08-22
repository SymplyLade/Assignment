# USING "IF", "ELSE" AND "ELIF"
print(" Welcome to Symply_Moren Network Service Bot!")
print("Dial *930#")
print("\nPlease choose your option:")
print("1. Recharge")
print("2. Data")
print("3. Exit")
option = input("Enter option: ")
if option == "1":
    print("\nYou selected Recharge :")
    print("Available amounts: 100, 200, 300, 400, 500, 1000")
    amount = input("Enter amount: ")
    if amount in ["100", "200", "300", "400", "500", "1000"]:
        print(f"You have successfully purchased ₦{amount} recharge card.")
    else:
        print("Invalid amount. Please choose from the listed options.")
elif option == "2":
    print("\nYou selected Data :")
    print("Available plans:")
    print("1. 500MB - ₦500")
    print("2. 1.5GB - ₦750")
    print("3. 3GB - ₦2500")
    print("4. 10GB - ₦5000")
    data_plan = input("Enter number for dataplan: ")
    if data_plan == "1":
        print("You have successfully purchased 500MB for ₦500.")
    elif data_plan == "2":
        print("You have successfully purchased 1.5GB for ₦750.")
    elif data_plan == "3":  
        print("You have successfully purchased 3GB for ₦2500.")
    elif data_plan == "4":
        print("You have successfully purchased 10GB for ₦5000.")
    else:
        print(" Invalid plan selected.")
elif option == "3":
    print("\nThank you for using Symply_Moren Network Service. Goodbye!")
else:
    print(" Invalid option! Please select 1, 2, or 3.")