# Password Strength Checker
## 📌 Overview

  This Python script evaluates the strength of a password based on several criteria and provides feedback for improvement. The script checks for:

📝 Minimum length

🔠 Uppercase letters

🔡 Lowercase letters

🔢 Numbers

🔒 Special characters

Based on these factors, the script assigns a strength rating (Very Weak to Very Strong) and gives feedback on how to improve weak passwords.

##🚀 Features

  🔒 Password strength evaluation: Checks against 5 key criteria.

  🛠️ Detailed feedback: Provides suggestions for improvement.

   🎨 Colorful output: Displays password strength in color (Green for strong, Red for weak).

   📊 Progress bar: Displays a progress bar while assessing the password.

## 🛠️ Requirements

  Python 3.x

  No external dependencies required (Standard Python library)

## 📜 Usage

  Clone the repository:

    git clone https://github.com/hf3cyber/PRODIGY_CS_03.git
    cd PRODIGY_CS_03

# Run the script:

    python pass_strength.py

  Enter a password when prompted, and the script will assess its strength.

### Example 1:

```
Enter a password to assess: P@ssw0rd
Password Strength: ########## 100%

Password Strength: Very Strong
Great job! Your password is strong!
```

### Example 2:

```
Enter a password to assess: password
Password Strength: ########## 10%

Password Strength: Weak

Feedback:
- Password should contain at least one uppercase letter.
- Password should contain at least one number.
- Password should contain at least one special character.
```

## 📧 Contact

For any questions or improvements, feel free to contribute or open an issue on the repository!

## 📝 License

This project is licensed under the [MIT License](./LICENSE).

