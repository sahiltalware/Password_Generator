import secrets
import string


# Function to Generate Strong Password
def generate_password(length):
    # Check if password length is less than 8 characters
    if length < 8:
        print("Password length should be at least 8 characters for security.")
        return None

    # Define the alphabet containing lowercase letters, uppercase letters, digits, and punctuation
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Loop until a strong password is generated
    while True:
        # Generate a password using randomly chosen characters from the alphabet
        password = ''.join(secrets.choice(alphabet) for i in range(length))

        # Check if the generated password meets modern security standards
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            break
    return password

# Function to generate multiple strong passwords.
def generate_multiple_passwords(num_passwords, length):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

# Main function to interact with the user and generate passwords.


def main():
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter desired password length: "))

        if num_passwords < 1:
            print("Please enter a number greater than 0 for the number of passwords.")
            return

        # Generate the passwords and display them
        print("\nGenerated Passwords:")
        passwords = generate_multiple_passwords(num_passwords, password_length)
        for i, password in enumerate(passwords, start=1):
            print(f"Password {i}: {password}")

    except ValueError:
        print("Please enter valid integers for the number of passwords and password length.")


if __name__ == "__main__":
    main()