#server.py
import Pyro4

@Pyro4.expose
class Temperature:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

daemon = Pyro4.Daemon()
uri = daemon.register(Temperature())

print("Temperature Server is running")
print("Server URI:", uri)

daemon.requestLoop()

#client.py
import Pyro4

uri = input("Enter server URI: ")
server = Pyro4.Proxy(uri)

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = server.celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit:", fahrenheit)
