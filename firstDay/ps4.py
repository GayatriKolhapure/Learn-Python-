import os

#select the directory whose content path you want to list
directory_path = "/"

# use the os module to list the directory content
contents = os.listdir(directory_path)

for item in contents:
    print(item)