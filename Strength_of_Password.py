#check strength of password
def password():
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Weak password: Too short (minimum 8 characters).")
    else:
        has_upper = False
        has_digit = False
        has_special = False
        special_chars = "!@#$%^&*(),.?\":{}|<>"

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
            elif char in special_chars:
                has_special = True

        if not has_upper:
            print("Weak password: Add at least one uppercase letter.")
        elif not has_digit:
            print("Weak password: Add at least one number.")
        elif not has_special:
            print("Weak password: Add at least one special character.")
        else:
            print("Strong password")
password()