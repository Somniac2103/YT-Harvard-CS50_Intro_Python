students = ["Hermoine", "Harry", "Ron"]

for student in students:
  print(student)

for i in range(len(students)):
  print(students[i])

students = {
  "Hermione": "Gryffindor",
  "Harry" : "Gryffindor",
  "Ron": "Gryffindor",
  "Draco": "Slytherin",  
}

print(students["Hermione"])

for student in students:
  print(student, students[student])


students = [
  {
    "name" : "Hermione",
    "house" : "Gryffindor",
    "patronus" : "Otter"  
  },{
    "name" : "Harry",
    "house" : "Gryffindor",
    "patronus" : "Stag" 
  },{
      "name" : "Ron",
      "house" : "Gryffindor",
      "patronus" : "Terrier" 
  },{
    "name" : "Draco",
    "house" : "Slytherin",  
    "patronus" : None,
  }
]

print(students[1]["name"])

for student in students:
  print(student["name"], student["house"], sep=", ")