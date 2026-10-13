class Process:
    def __init__(self, pid, n):
        self.pid = pid
        self.n = n
        self.clock = 0
        self.request_time = 0
        self.requesting = False
        self.reply_count = 0
        self.deferred = []

    def receive_reply(self, sender):
        self.reply_count += 1
        print(f"Process {self.pid} receives REPLY from {sender}")

    def receive_request(self, sender, timestamp):
        self.clock = max(self.clock, timestamp) + 1

        print(f"Process {self.pid} receives REQUEST from {sender}")

        if not self.requesting:
            processes[sender].receive_reply(self.pid)

        elif (timestamp, sender) < (
            self.request_time, self.pid
        ):
            processes[sender].receive_reply(self.pid)

        else:
            self.deferred.append(sender)


def simulate(n, request_ids):
    global processes
    processes = [Process(i, n) for i in range(n)]

    # All requesting processes announce their requests first.
    for pid in request_ids:
        p = processes[pid]
        p.clock += 1
        p.request_time = p.clock
        p.requesting = True
        print(f"Process {pid} sends REQUEST")

    # Deliver all REQUEST messages.
    for pid in request_ids:
        p = processes[pid]

        for other in processes:
            if other.pid != pid:
                other.receive_request(pid, p.request_time)

    # Processes enter the CS in timestamp/ID priority order.
    order = sorted(
        request_ids,
        key=lambda pid: (
            processes[pid].request_time, pid
        )
    )

    for pid in order:
        p = processes[pid]

        while p.reply_count < n - 1:
            pass

        print(f"\nProcess {pid} enters Critical Section")
        print(f"Process {pid} exits Critical Section")
        p.requesting = False

        # Send deferred replies after leaving the CS.
        for sender in p.deferred:
            processes[sender].receive_reply(pid)

        p.deferred.clear()

    print("\nAll requests completed.")


simulate(3, [0, 1, 2])