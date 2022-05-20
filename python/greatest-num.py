# Python program that finds the greatest of n numbers

try:
    count = int(input("Number count: "))

except ValueError:
    print("Invalid count")
    quit()

num_list = []

for i in range(count):
    try:
        num_list.append(float(input(f"Type a number: ")))

    except ValueError:
        print("Invalid number")

print(f"Greatest value is: {max(num_list)}")
