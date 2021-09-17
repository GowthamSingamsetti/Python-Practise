from pathlib import Path


# There are 2 types of path
# Absolute path = We start from the root of the hard disk. In windows we have absolute path like c:\Program Files\bin
# Relative path = A path starting from currrent directory and go somewhere else
# If nothing is given in double quotes it starts from the current path

path = Path("shoppingmall")
print(path.exists())

# path2 = Path("Theatre")
# path2.mkdir()
# path2.rmdir()

path3 = Path()
# print(path3.glob('*.py'))
for file in path3.glob('*.py'):
    print(file)

# To iterate all files in a directory and process them
# Path() is for current directory
# with glob method we can search for files and directories in the current path
# we can use glob method to search for files using a pattern
# we should pass a string for the first argument that defines a search pattern
# '*' means all files and all directories. '*.*' for all the files in the current directory but not all the directories
#