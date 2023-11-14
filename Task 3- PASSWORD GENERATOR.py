import random
import string

def generate_password(length, complexity):
    characters = ""

    if complexity >= 1:
        characters += string.ascii_lowercase  # lowercase letters
    if complexity >= 2:
        characters += string.ascii_uppercase  # uppercase letters
    if complexity >= 3:
        characters += string.digits  # digits
    if complexity >= 4:
        characters += string.punctuation  # symbols

    if not characters:
        print("Invalid complexity. Please choose a complexity level between 1 and 4.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
        complexity = int(input("Enter the complexity level (1-4): "))

        if 1 <= complexity <= 4:
            password = generate_password(length, complexity)
            if password:
                print(f"Generated Password: {password}")
        else:
            print("Invalid complexity level. Please choose a complexity level between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()

