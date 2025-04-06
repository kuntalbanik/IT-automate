import os

def list_files_walk(start_path='.'):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            print(os.path.join(root, file))

# Specify the directory path you want to start from
directory_path = './'
list_files_walk(directory_path)
