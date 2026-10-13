
import threading
import time

n = int(input("Enter number of processes: "))
token = 0
lock = threading.Lock()
condition = threading.Condition(lock)

def process(pid):
    global token

    with condition:
        while token != pid:
            condition.wait()

        print(f"P{pid} receives TOKEN")
        print(f"P{pid} ENTERS Critical Section")

    time.sleep(1)

    with condition:
        print(f"P{pid} LEAVES Critical Section")

        token = (pid + 1) % n
        print(f"P{pid} passes TOKEN to P{token}\n")

        condition.notify_all()

threads = []

for i in range(n):
    t = threading.Thread(target=process, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All processes completed.")
