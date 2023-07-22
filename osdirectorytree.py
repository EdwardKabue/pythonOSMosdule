import os

#change directory
os.chdir("/home/code7/")

#traverse directory tree
# for dirpath, dirnames, filenames in os.walk("/home/code7/"):
#   print("Current path:", dirpath)
#   print("Directories:", dirnames)
#   print("Files:", filenames)
#   print()

#get environment variables
#print(os.environ.get("HOME"))

#create file path from directory and file strings.
file_path = os.path.join(os.environ.get("HOME"), "test.txt")
#print(file_path)

#get basename (final component of path name)
print(os.path.basename(file_path))

#get directory from path name
print(os.path.dirname(file_path))

#get both directory name and final component name
print(os.path.split(file_path))

#check if path exists.
print(os.path.exists(file_path))

#check if path name points to a file.
print(os.path.isfile(file_path))

#split path name and extension
print(os.path.splitext(file_path))
