# WORD ANALYSER
answer = "ikeja"
while True:
    try:
        capital = input("Enter the capital of Lagos state: ").strip()
        # Control flow checks
        if capital.lower() == answer:
            print("\nCorrect!!!")
            break
        elif capital.upper() == answer.upper():
            print("\nCorrect!!!")
            break
        elif capital.title() == answer.title():
            print("\nCorrect!!!")
            break
        else:
            print("\nIncorrect!!! Try again.")
    except KeyboardInterrupt:
        print("\n\n:warning: You interrupted the quiz. Exiting...")
        break
    except EOFError:
        print("\n\n:warning: Input was closed unexpectedly. Exiting...")
        break
    except Exception as e:
        print(f"\n Unexpected error: {e}")
        break