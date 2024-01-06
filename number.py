# ValueError = incorrect value provided
# NameError = variable not defined
def main():
  x = get_int()
  print(f"X is {x}")

def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      #pass
      print(f"{prompt} is not an integer")
    else:
      break
  return x

main(prompt)