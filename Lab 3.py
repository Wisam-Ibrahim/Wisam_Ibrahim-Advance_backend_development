#__init__ instance attributes
print("__init__ instance attributes")
class person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

person1 = person("Ali", 25)
person2 = person("Omar", 30)

print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)

#instance methods vs class attributes
print("instance methods vs class attributes")
class Student:
  school = "ABC School"

  def __init__(self,name,age):
    self.name = name
    self.age = age

  def introduce(self):
    print( f"my name is {self.name}")
    print( f"I am{self.age} years old")
    print( f"I study at{Student.school}")



student1 = Student("Wisam", 25)
student2 = Student("Ibrahim", 40)

student1.introduce()
student2.introduce()


#Inheritance & super()
print("Inheritance & super()")
class Animal:

  def __init__(self,name):
    self.name = name

  def speak(self):
    print( f"{self.name} makes a sound")


class Dog (Animal):
  def __init__(self,name,breed):
    super().__init__(name)
    self.breed = breed

  def speak(self):
    super().speak()
    print( f"{self.name} barks")

dog = Dog("Max", "Labrador")

print(dog.name)
print(dog.breed)

dog.speak()
