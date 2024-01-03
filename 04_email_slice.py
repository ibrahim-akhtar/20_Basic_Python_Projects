# Project 04
# Email Slicer

email = input("Enter your email: ")
flag = 1
username = ""
domain = ""
for i in email:
    ch = i

    if ch != '@' and flag == 1:
        username += ch
    elif ch != '@' and flag == 0:
        domain += ch
    else:
        flag = 0
        continue

# OR
# username, domain = email.split("@")

domain, extension = domain.split(".")

print("Username:", username)
print("Domain:", domain)
print("extension:", extension)