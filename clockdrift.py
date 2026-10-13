clock_a = 0
clock_b = 0

drift_rate = 10       # milliseconds per second
duration = 60         # one minute

for second in range(1, duration + 1):
    clock_a += 1000
    clock_b += 1000 + drift_rate

    if second % 10 == 0:
        print("Time:", second, "seconds")
        print("Clock A:", clock_a, "ms")
        print("Clock B:", clock_b, "ms")
        print("Difference:", clock_b - clock_a, "ms")
        print()

print("Final clock difference:", clock_b - clock_a, "milliseconds")
