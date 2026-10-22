"""Generate strong random passwords from user-selected complexity levels."""

import secrets
import string


def get_password_length():
    """Ask for a valid password length."""
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length >= 4:
                return length
            print("Please enter a length of at least 4.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_complexity():
    """Let the user choose which character groups to include."""
    print("\nChoose password complexity:")
    print("1. Easy   - lowercase letters")
    print("2. Medium - lowercase and uppercase letters, numbers")
    print("3. Strong - lowercase and uppercase letters, numbers, symbols")

    while True:
        choice = input("Enter choice (1-3): ").strip()
        groups = {
            "1": [string.ascii_lowercase],
            "2": [string.ascii_lowercase, string.ascii_uppercase, string.digits],
            "3": [
                string.ascii_lowercase,
                string.ascii_uppercase,
                string.digits,
                string.punctuation,
            ],
        }
        if choice in groups:
            return groups[choice]
        print("Please choose 1, 2, or 3.")


def generate_password(length, character_groups):
    """Generate a password containing at least one character from each group."""
    all_characters = "".join(character_groups)
    password = [secrets.choice(group) for group in character_groups]
    password.extend(secrets.choice(all_characters) for _ in range(length - len(password)))
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def main():
    print("--- Password Generator ---")

    while True:
        length = get_password_length()
        character_groups = get_complexity()
        password = generate_password(length, character_groups)

        print("\nYour generated password is:")
        print(password)

        again = input("\nGenerate another password? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Stay safe and keep your password private!")
            break


if __name__ == "__main__":
    main()
