import os

def remove_file(file_name):
    if os.path.exists(file_name) is True:
        os.remove(file_name)
