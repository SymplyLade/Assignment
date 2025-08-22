# check if a string starts with https://
while True:
    try:
        url = input("Enter a URL: ").strip()
        # Control flow check for "https://"
        if url.startswith("https://"):
            print("\n:white_check_mark: Welcome! Valid URL.")
            break
        else:
            print(":x: Incorrect URL! Must start with 'https://'\n")
    except KeyboardInterrupt:
        print("\n\n:warning: Program interrupted by user (Ctrl + C). Exiting...")
        break
    except EOFError:
        print("\n\n:warning: Input stream closed unexpectedly (Ctrl + D / Ctrl + Z). Exiting...")
        break
    except Exception as e:
        print(f"\n:x: Unexpected error occurred: {e}")