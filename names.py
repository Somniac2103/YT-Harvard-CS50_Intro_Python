# name = input("What is your name? ")

# with open("names.txt","a") as file:
#   file.write(f"{name}\n")

names = []

with open("names.txt", "r") as file:
  for line in file:
  #   print("hello,", line.rstrip())
    names.append(line.rstrip())

for name in sorted(names):
  print(f"hello, {name}")

