import os
import shutil

address = input("Enter the address (path): ")
files = os.listdir(address)

for file in files:
    filename, fileFormat = os.path.splitext(file)
    ext = fileFormat[1:]

    if os.path.exists(address + '/' + ext):
        shutil.move(address + '/' + file, address + '/' + ext + '/' + file)
    else:
        os.makedirs(address + '/' + ext)
        shutil.move(address + '/' + file, address + '/' + ext + '/' + file)