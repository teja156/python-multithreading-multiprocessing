# Program to crack a SHA256 password hash using a single thread

import time
import hashmaker
from exectime import calculate_execution_time

@calculate_execution_time
def crackpass(hash):
    # Read all lines from rockyou.txt
    with open("rockyou.txt", "r", encoding="latin-1") as f:
        lines = f.readlines()
        # Iterate through each line
        for ind, line in enumerate(lines):
            # print(f"[{ind}/{len(lines)}] ({ind/len(lines)*100:.2f}%)", end='\r')
            line = line.replace("\n", "")
            line = line.strip()
            # Check if hash matches
            if hashmaker.SHA256(line).strip() == hash.strip():
                print("\nHash found!")
                print(f"Password: {line}")
                # return line

crackpass("4ca83ed9af3a129e949c72a67cb7fcb0c11094d2f541c7b0a8e60ee2fe6d3c25")