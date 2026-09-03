import random

name = input("Enter your name: ")

number = random.randint(1, 9)

print("\nHello", name)
print("Your lucky number is:", number)

if number in [7, 8, 9]:
    print("Today may be a lucky day!")
else:
    print("Keep working hard and stay positive!")
    