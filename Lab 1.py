 #Basic
name = 'Wisam'   #string
age = 24   
cgpa = 3.5
student = True

print(name)
print(age)
print(cgpa)
print(student)

#input
sgpa = float(input('Enter SGPA: '))

#if & if-else = elif & else
if sgpa >= 3.5:
    print("Grade: A")
elif sgpa >= 3:
    print("Grade: B")
elif sgpa >= 2.5:
    print("Grade: C")
elif sgpa >= 2:
    print("Grade: D")
else:
    print("Grade: F")

# for loop
j = input('Enter a number: ')


for i in range(1, int(j) + 1):
    print(i)
#  while loop  
i = 1

while i <= int(j):
    print(i)
    i += 1

#function   
def function1():
    print("Hello student!")

function1()

def hello(name):
    print("Hello", name)

hello("Ibrahim")

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

def numbers(j):
    i = 1
    while i <= j:
        print(i)
        i += 1

numbers(5)
