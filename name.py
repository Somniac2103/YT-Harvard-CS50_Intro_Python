import sys

if len(sys.argv) < 2:
  sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#   sys.exit("Too many arguments")
# else:
#try:
  #print("hello, my name is ",sys.argv[1])
#except IndexError:
#  print("Too few arguments")

for arg in sys.argv[1:-1]:
  print("hello,", arg)