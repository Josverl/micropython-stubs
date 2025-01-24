import os

# Create a new file and write to it
with open("newfile.txt", "w") as f:
    f.write("Hello, world!")

# Append to the existing file
with open("newfile.txt", "a") as f:
    f.write("\nAppending a new line.")

# Read the file
with open("newfile.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# Rename the file
os.rename("newfile.txt", "renamedfile.txt")

# # Check if the file exists
# if os.path.exists("renamedfile.txt"):
#     print("File exists.")

# Remove the file
os.remove("renamedfile.txt")

# Create a new directory
os.mkdir("newdir")

# List contents of the directory
print("Directory contents:", os.listdir("newdir"))

# Remove the directory
os.rmdir("newdir")
