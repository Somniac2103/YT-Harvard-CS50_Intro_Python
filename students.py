import csv

name = input("Name?")
home = input("Home?")

with open("students.csv", "a") as file:
  writer = csv.DictWriter(file, fieldnames= ["name", "home"])
  writer.writerow({"name": name, "home": home})



# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     print(f"{name} is in {house}")

# students = []

# with open("students.csv") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     students.append({"name": row["name"], "house" : row["house"]})
#   for line in file:
#     name, house = line.rstrip().split(",")
# #     students.append(f"{name} is in {house}")
#     student = {"name": name, "house":house}
#     student.append(student)

# for student in sorted(students):
#   print(student)
    
    # student = {}
    # student["name"] = name
    # student["house"] = house
    # student.append(student)

# def get_name(student):
#   return student["name"]

# for student in sorted(students, key = lambda student: student["name"]):
#   print(f"{student['name']} is from {student['house']}")