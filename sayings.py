def main(name):
  hello(name)
  goodbye(name)

def hello(name):
  print(f"hello, {name}")

def goodbye(name):
  print(f"goodbye, {name}")


if __name__=="__main__":
    main("Barry")