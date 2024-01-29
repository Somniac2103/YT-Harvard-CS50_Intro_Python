import re

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/","")
# username = url.removeprefix("https://twitter.com/")

re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# print(url)
print(f"Username: {username}")
