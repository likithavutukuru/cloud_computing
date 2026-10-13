# Round Robin Task Scheduling

n = int(input("Enter number of tasks: "))

tasks = []

for i in range(n):
    time = int(input(f"Enter processing time for Task {i+1}: "))
    tasks.append(time)

workers = [0, 0]       # Completion time of each worker
count = [0, 0]         # Number of tasks assigned
completion = []

for i in range(n):
    worker = i % 2     # Round Robin assignment

    workers[worker] += tasks[i]
    count[worker] += 1

    completion.append(workers[worker])

    print(f"Task {i+1} assigned to Worker {worker+1}")
    print(f"Processing time: {tasks[i]} seconds")
    print(f"Completion time: {completion[i]} seconds")
    print()

print("----- FINAL RESULTS -----")

print("Worker 1 tasks:", count[0])
print("Worker 2 tasks:", count[1])

print("Worker 1 completion time:", workers[0], "seconds")
print("Worker 2 completion time:", workers[1], "seconds")

print("Total execution time:", max(workers), "seconds")
