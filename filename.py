# Accept the filename from the user
filename = input("Enter a filename: ")

# Split the filename using dot
parts = filename.split(".")

# Check if there is at least one dot in the filename
if len(parts) > 1:
    # The last element in the list is the file extension
    extension = parts[-1]
    print(f"The file extension is: {extension}")
else:
    print("This filename does not have an extension.")
# Extension here is mostly (.py)
