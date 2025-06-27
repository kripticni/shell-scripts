import os

directory_path = input("Path to dir: ")

for root, dirs, files in os.walk(directory_path):
    for file in files:
        print(os.path.join(root, file))
