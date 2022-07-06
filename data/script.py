#!/usr/bin/env python3

import sys
import os
import shutil

def organize_ovpn_into_dir(path):
    for operand in os.scandir(path):
        if(operand.is_file()):
            directory = operand.name[0:2]
            file_name = operand.name
            if(file_name[-4:] == "ovpn"):
                os.makedirs(directory, exist_ok=True)
                shutil.copyfile(file_name, directory + "/" + file_name)
                os.remove(file_name)

def main():
    path = "."
    organize_ovpn_into_dir(path)

if __name__ == "__main__":
    main()

