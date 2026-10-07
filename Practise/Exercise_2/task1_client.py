import Pyro4
# uri = input("Enter Server URI: ")
# calculator = Pyro4.Proxy(uri)
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("Addition:", calculator.add(a, b))
# print("Multiplication:", calculator.multiply(a, b))

uri = input("Enter the uri: ")

calculator = Pyro4.Proxy(uri)
print("Addition:", calculator.add(10, 20))

print("Multiplication:", calculator.multiply(10, 20))