class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def print_name(self):
    print("Name is " + self.name)

person = Person("Harsh", 29)
person.print_name()
