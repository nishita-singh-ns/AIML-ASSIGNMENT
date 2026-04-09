### CODE CELL ###
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

if age < 13:
    category = "a Child"
elif age < 20:
    category = "a Teenager"
elif age < 60:
    category = "an Adult"
else:
    category = "a Senior Citizen"

print("\nHello", name + "!")
print("You are", category + ".")
print("It's great that you enjoy", hobby + "!")

### CODE CELL ###


