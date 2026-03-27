# Smart Input Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Age categorization
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print("\nHello", name)
print("You are categorized as:", category)
print("It's great that you enjoy", hobby)