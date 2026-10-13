class Process:
    def __init__(self, pid, n):
        self.pid = pid
        self.vector = [0] * n

    def event(self):
        self.vector[self.pid] += 1
        print(f"P{self.pid+1} event: {self.vector}")

    def send(self):
        self.vector[self.pid] += 1
        print(f"P{self.pid+1} sends: {self.vector}")
        return self.vector.copy()

    def receive(self, message):
        for i in range(len(self.vector)):
            self.vector[i] = max(
                self.vector[i], message[i]
            )

        self.vector[self.pid] += 1
        print(f"P{self.pid+1} receives: {self.vector}")


p1 = Process(0, 3)
p2 = Process(1, 3)
p3 = Process(2, 3)

n = int(input("Enter internal events in P1: "))
for i in range(n):
    p1.event()

msg1 = p1.send()
p2.receive(msg1)

n = int(input("Enter internal events in P2: "))
for i in range(n):
    p2.event()

msg2 = p2.send()
p3.receive(msg2)

n = int(input("Enter internal events in P3: "))
for i in range(n):
    p3.event()

msg3 = p3.send()
p1.receive(msg3)

print("\nFinal Vector Clocks:")
print("P1:", p1.vector)
print("P2:", p2.vector)
print("P3:", p3.vector)
