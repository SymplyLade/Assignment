# QUESTION 1    
# Explain each output of the program below.
# Give 3 usecases or scenarios where you can apply the program below.
# Write the code for 1 of the 3 use cases.

#num1 = int(input("Enter first number:"))
#num2 = int(input("Enter second number:"))
#print(f"{num1} == {num2} : {num1 == num2}")
# Output: 4 ==5 : False because {num1} is not equal to {num2}

#print(f"{num1} != {num2} : {num1 != num2}")
 # Output: 4 != 5 : True because 4 is not equal to 5

#print(f"{num1} > {num2} : {num1 > num2}")
# Output: 4 > 5 : False because 4 is not greater than 5

#print(f"{num1} < {num2} : {num1 < num2}")
# Output 4 < 5 : True because 4 is less than 5

# Give 3 usecases scenarios where you can apply the program below.
# Student Exam Result
# To check Age Eligibility
# To cut-off marks

#  Write the code for 1 of the 3 use cases
print("TO Proceed to this football training college,we need to confirm your age")
user_input = int(input("Enter your age:"))
age = 16    # Defined variable
eligibility = (user_input < age)
print(" You are eligible to proceed", (eligibility))