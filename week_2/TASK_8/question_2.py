# Federal Government Scholarship Enrollment
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score:"))
# Citizenship
citizenship_status = input("Enter your Citizenship: ").lower()
# Enrollment
enrollment = input("Are you a student of any Nigeria university?(Yes/No):").lower()
# Other Scholarships
other_scholarship = input("Are you receiving any other scholarship?(Yes/No):").lower()
# Academic Qualification
distinction = int(input("How many (A/B) do you have in your WAEC/WASSCE?:"))

# Eligibility
from_nigeria = (citizenship_status == "nigerian")
is_enrolled = (enrollment == "yes")
receiving_another_scholarship = (other_scholarship == "no")
required_distinction = (distinction >= 5)
eligibility = (from_nigeria and is_enrolled and receiving_another_scholarship and required_distinction)
print(f"Name: {name}\nAge: {age}\nScore: {score}\nCitizenship: {citizenship_status}\nEligibility: {eligibility}")
print(f"\n{name},Your scholarship eligibility is: {eligibility}")