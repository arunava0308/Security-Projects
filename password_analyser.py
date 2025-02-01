import hashlib

""" Parameters Defined """
password = input("Enter the password :: ")
hashed = ''
points = 0
labels = []

""" Check Password Length"""
if len(password) >= 8:
    points += 2
    labels.append("Password length is good")
else:
    points -= 2
    labels.append("Make password atleast 8 characters long")

    
""" Check Number of Uppercase, Lowercase, Digits & Special Characters"""
l = {"uppercase":0, "lowercase":0, "digit":0, "special":0}
for i in range(len(password)):
    if password[i].isupper():
        l["uppercase"] += 1
    elif password[i].islower():
        l["lowercase"] += 1
    elif password[i].isdigit():
        l["digit"] += 1
    else:
        l["special"] += 1
    
for i in l:
    if l[i] > 3:
        points += 2
    elif l[i] >= 1 and l[i] <=3:
        points += 1
    if l[i] == 0:
        arg = "Their is no " + i + " character"
        labels.append(arg)
        
""" Converting into Hash and checking against rockyou.txt """
target_hash = hashlib.sha256(password.encode()).hexdigest()
wordlist_path = "/usr/share/wordlists/rockyou.txt"

with open(wordlist_path, "r", encoding="latin-1") as file:
    for passkey in file:
        passkey = passkey.strip()
        hashed_passkey = hashlib.sha256(passkey.encode()).hexdigest()
        if hashed_passkey == target_hash:
            labels.append("Password found in wordlist.")
            points -= 5
            break
    else:
        points += 5
        labels.append("Password not found in wordlist")

if points >= 11:
    print("\nPassword is STRONG")
    print("Here's an overview of the password :: ")
    for i in labels:
        print(i)
else:
    print("\nPassword is WEAK. Please change the password\n")
    print("Here's an overview of the password :: ")
    for i in labels:
        print(i)

#                                                           ~Arunava@0308