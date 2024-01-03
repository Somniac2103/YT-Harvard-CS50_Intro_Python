i = 0
while i < 3:
  print("meow")
  i += 1

for i in [0,1,2]:
  print("bark")

for _ in range(3):
  print("oik")

print("beh\n" *3, end="")

while True:
  n = int(input("What is N?"))
  if n > 0:
    break

for _ in range(n):
  print("Howl")


def main():
  number = get_number()  
  boo(number)

def get_number():
  while True:
    n = int(input("what is n?"))
    if n > 0:
      return n

def boo(n):
  for _ in range(n):
    print("Boo")

main()