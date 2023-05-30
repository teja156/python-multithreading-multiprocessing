import time
import hashmaker
import threading
from exectime import calculate_execution_time

CRACKED = False
print_lock = threading.Lock()

def crackpass(chunk, hash):
    global CRACKED
    # Read all lines from rockyou.txt
    for ind, line in enumerate(chunk):
        if CRACKED:
            return 
        # print_lock.acquire()
        # print(f"[{ind}/{len(chunk)}] ({ind/len(chunk)*100:.2f}%)", end='\r')
        # print_lock.release()
        line = line.replace("\n", "")
        line = line.strip()
        # Check if hash matches
        if hashmaker.SHA256(line).strip() == hash.strip():
            print("\nHash found!")
            print(f"Password: {line}")
            CRACKED = True
            # return line

@calculate_execution_time
def main():
    hash = "4ca83ed9af3a129e949c72a67cb7fcb0c11094d2f541c7b0a8e60ee2fe6d3c25"
    num_threads = 4
    threads = []
    # Split rockyou.txt into 4 chunks
    chunks = []
    with open("rockyou.txt", "r", encoding="latin-1") as f:
        lines = f.readlines()
        chunk_size = len(lines) // num_threads
        chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]

    # Create threads
    for i in range(num_threads):
        t = threading.Thread(target=crackpass, args=(chunks[i], hash, ))
        t.daemon = True
        t.start()
        threads.append(t)
    

    # Wait for threads to finish
    for t in threads:
        t.join()


main()
