import re

email = input("Email?").strip()

if re.search(r"^\w+@\w+\.edu$", email,re.IGNORECASE):

# if "@" and "." in email:

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
  print("Valid")
else:
  print("Invalid")