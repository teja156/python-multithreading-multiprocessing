# Singlethread vs Multithreading vs Multiprocessing


[Watch YouTube video](https://youtu.be/qFr_nQZWl7o)
Code written to demonstrate the performance difference between single threading, multi threading and multi processing in Python.

## Code
The code tries to crack a SHA256 password hash with the help of the wordlist `rockyou.txt` using dictionary attack.
You will need to download rockyou.txt manually from (here)[https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt] and add it to the code path.
singlethread.py - Code written for single thread (ie., a normal program)
multithread.py - Code written to work with 4 threads
multiprocess.py - Code written to work with 4 processes


## Conclusion from the experiment
- If you're writing a CPU bound program (tasks that need more CPU power): Go with singlethread program instead of multithreading. Multithreading only adds a overhead and doesn't improve the performance of your code, because multithreaded code in Python runs as a single thread code due to Python's Global Interpreter Lock (GIL). It only increases the execution time and makes your code worse because thread switching and locks only add more overhead. If you want to utilize multiple cores of your CPU, go ahead with multiprocessing. Also note that multiprocessing is only ideal when there is not much inter-process communication between the processes. Inter-process communication needs more computing resources because the data transmitted between the processes need to be serialized (on sender side) and de-serialized (on receiver side). So when there is a lot of inter-process communication, multiprocessing can actually make your code perform worse than a single thread program.
- If you're writing an I/O bound program (tasks that wait for I/O operations from external resources): Go with multithreading. When one thread is waiting for an I/O operation from an external source (like a file, database, website response, etc), another thread can come into the execution state and do its task while the other thread is waiting. Therefore, waiting times can be eliminated. This improves the performance of the code.
- SIDE BUT IMPORTANT NOTE: DO NOT use the `print()` function recklessly, it adds much more overhead than you think.

