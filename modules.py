import random
import re
import string

def genrate_password(length,digit,symbol):
    password = string.ascii_letters
    if digit and symbol:
        password += string.digits + string.punctuation
    elif symbol:
        password += string.punctuation
    elif digit:
        password += string.digits
        
    return ''.join(random.choice(password) for _ in range(length))

def password_checker(user_password):

    check = 0
    message = []

    if user_password:
        if len(user_password) >= 8:
            check+=1
        else:
            message.append("Atleast password must be contain 8 character and longer")
        if re.search("[A-Z]" , user_password):
            check+=1
        else:
            message.append("Atleast 1 Uppercase character")
        if re.search("[a-z]" , user_password):
            check+=1
        else:
            message.append("Atleast 1 Lowercase character")
        if re.search("\d" , user_password):
            check+=1
        else:
            message.append("Atleast 1 digit number")
        if re.search("[^a-zA-Z0-9]" , user_password):
            check+=1
        else:
            message.append("Atleast 1 special character")

    if check <= 2:
        strength = "Weak"
    elif check <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, message