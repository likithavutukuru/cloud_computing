#server.py

import Pyro4

@Pyro4.expose
class Calculator:
    def add(self,a,b):
        return a+b

    def multiply(self, a, b):
        return a*b

daemon = Pyro4.Daemon()

calculator = Calculator()

uri = daemon.register(calculator)

print("Calculator is ready.")
print("URI:", uri)

daemon.requestLoop()

#client.py
import Pyro4

uri = input("Enter the uri: ")

calculator = Pyro4.Proxy(uri)
print("Addition:", calculator.add(10, 20))

print("Multiplication:", calculator.multiply(10, 20))