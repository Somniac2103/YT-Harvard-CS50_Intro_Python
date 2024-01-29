import re

name = input("Name?").strip()
if matches := re.search(r"^(.+), *(.+)$", name):

# if matches:
  # last, first = matches.groups()
  # name = f"{first} {last}"
  name = matches.group(2) + " " + matches.group(1)
# if "," in name:
#   last, first = name.split(", ")
#   name = f"{first} {last}"

print(f"hello, {name}")

