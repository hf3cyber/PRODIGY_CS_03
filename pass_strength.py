import re
import time

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None
    
    # Calculate score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    # Assess strength
    if score == 5:
        strength = "Very Strong"
        strength_color = Colors.GREEN
    elif score == 4:
        strength = "Strong"
        strength_color = Colors.YELLOW
    elif score == 3:
        strength = "Moderate"
        strength_color = Colors.YELLOW
    elif score == 2:
        strength = "Weak"
        strength_color = Colors.RED
    else:
        strength = "Very Weak"
        strength_color = Colors.RED

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character.")
    
    return strength, feedback, strength_color

def show_progress_bar():
    for i in range(101):
        print(f'\rPassword Strength: {"#" * (i // 10)}{" " * (10 - i // 10)} {i}%', end="")
        time.sleep(0.1)
    print()

# Main program
password = input("Enter a password to assess: ")
show_progress_bar()

strength, feedback, strength_color = assess_password_strength(password)

print(f"\nPassword Strength: {strength_color}{strength}{Colors.RESET}")

if feedback:
    print(f"\n{Colors.RED}Feedback:{Colors.RESET}")
    for item in feedback:
        print(f"- {item}")
else:
    print(f"{Colors.GREEN}Great job! Your password is strong!{Colors.RESET}")
