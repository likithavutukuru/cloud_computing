class Process:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0

    def event(self):
        self.clock += 1
        print(f"P{self.pid} event: Clock = {self.clock}")

    def send(self):
        self.clock += 1
        print(f"P{self.pid} sends message: Timestamp = {self.clock}")
        return self.clock

    def receive(self, timestamp):
        self.clock = max(self.clock, timestamp) + 1
        print(f"P{self.pid} receives message: Clock = {self.clock}")


p0 = Process(0)
p1 = Process(1)

n = int(input("Enter number of events in P0: "))
for i in range(n):
    p0.event()

timestamp = p0.send()

n = int(input("Enter number of events in P1: "))
for i in range(n):
    p1.event()

p1.receive(timestamp)

print("Final clock of P0:", p0.clock)
print("Final clock of P1:", p1.clock)
