email = input("Email?").strip()

# if "@" and "." in email:

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
  print("Invalid")