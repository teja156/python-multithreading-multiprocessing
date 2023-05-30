import multiprocessing
import hashmaker
from exectime import calculate_execution_time

def crackpass(chunk, hash):
    # Read all lines from rockyou.txt
    for ind, line in enumerate(chunk):
        # print(f"[{ind}/{len(chunk)}] ({ind/len(chunk)*100:.2f}%)", end='\r')
        line = line.replace("\n", "")
        line = line.strip()
        # Check if hash matches
        if hashmaker.DjangoCheckSHA256(line, hash):
            print("\nHash found!")
            print(f"Password: {line}")
            # return line

@calculate_execution_time
def main():
    # multiprocessing.freeze_support()
    hash = "4ca83ed9af3a129e949c72a67cb7fcb0c11094d2f541c7b0a8e60ee2fe6d3c25"
    num_processes = 4
    processes = []
    # Split rockyou.txt into 4 chunks
    chunks = []
    with open("rockyou.txt", "r", encoding="latin-1") as f:
        lines = f.readlines()

        chunk_size = len(lines) // num_processes
        chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]
    

    # Create processes
    for i in range(num_processes):
        p = multiprocessing.Process(target=crackpass, args=(chunks[i], hash, ))
        p.daemon = True
        processes.append(p)
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
    

    # Wait for processes to finish
    for p in processes:
        p.join()

if __name__ == '__main__':
    main()
