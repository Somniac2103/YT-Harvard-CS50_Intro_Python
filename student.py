class Student:
  def __init__(self, name, house):
    self.name = name
    self.house = house
    # self.patronus = patronus
  
  def __str__(self):
    return f"{self.name} from {self.house}"
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("Missing name")
    self._name = name

  # Getter
  @property
  def house(self):
    return self._house
  
  # Setter
  @house.setter
  def house(self, house):
    if house not in ["Gryffindor", "HufflePuff"]:
      raise ValueError("Invalid house")
    self._house = house
  
  # def charm(self):
  #   match self.patronus:
  #     case "Stag":
  #       return "stag"
  #     case _:
  #       return "puff"

  @classmethod 
  def get(cls):  
    name = input("Name: ")
    house = input("House: ")
    # patronus = input("Patronus: ")
    return cls(name, house)


def main():
  student = Student.get()
  # print(f"{student.name} from {student.house}")
  print(student)
  # print(student.charm())


if __name__ == "__main__":
  main()