import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Score based on how many checks it passes
    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    # Determine strength
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong 🔐"
    elif score == 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    # Collect feedback
    feedback = []
    if length_error:
        feedback.append("• At least 8 characters")
    if uppercase_error:
        feedback.append("• At least one UPPERCASE letter")
    if lowercase_error:
        feedback.append("• At least one lowercase letter")
    if digit_error:
        feedback.append("• At least one number")
    if special_char_error:
        feedback.append("• At least one special character (!@#$%^&*)")

    return strength, feedback


def main():
    print("=== 🔐 Password Strength Checker ===\n")
    while True:
        password = input("Enter a password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Goodbye!")
            break

        strength, feedback = check_password_strength(password)

        print("\nPassword Strength:", strength)

        if feedback:
            print("Suggestions to improve:")
            for item in feedback:
                print(item)
        else:
            print("Your password is secure!")

        print("\n" + "-" * 40)


if __name__ == "__main__":
    main()
 
