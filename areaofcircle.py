PI = 3.14
r = float(input(' Please Enter the radius of a circle: '))
area = PI * r * r
print(" Area Of a Circle = %.2f" %area)
# Accept the filename from the user
filename = input("Enter a filename: ")

# Split the filename with dot
parts = filename.split(".")
# There should be a dot and an extension
if len(parts) > 1:
    # The last element in the list is the file extension
    extension = parts[-1]
    print(f"The file extension is: {extension}")
else:
    print("This filename does not have an extension.")
