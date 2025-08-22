# : Word Analyzer
# - Ask the user to input a word.
# - Check if it is all uppercase, all lowercase, or title case.
# - Print the length of the word.
answer = "ikeja"
while True:
    capital = input("Enter the capital of Lagos state: ")
    if capital.lower() == answer:
        print("\nCorrect!!!")
    elif capital.upper() == answer:
        print("\nCorrect!!!")
    elif capital.title() == answer:
        print("\nCorrect!!!")
        break
    else:
        print("\nIncorrect!!!")