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