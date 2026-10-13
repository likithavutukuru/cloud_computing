#server.py
import Pyro4

@Pyro4.expose
class Shopping:
    def calculate_bill(self, product, quantity):
        prices = {
            "laptop": 50000,
            "mobile": 20000,
            "headphones": 2000
        }

        if product not in prices:
            return "Product not available"

        total = prices[product] * quantity
        discount = total * 0.10
        final_amount = total - discount

        return total, discount, final_amount

daemon = Pyro4.Daemon()
uri = daemon.register(Shopping())

print("Shopping server is running...")
print("Server URI:", uri)

daemon.requestLoop()

#client.py
import Pyro4

uri = input("Enter server URI: ")
shop = Pyro4.Proxy(uri)

total_bill = 0
total_discount = 0

while True:
    product = input("\nEnter product name (or exit): ").lower()

    if product == "exit":
        break

    quantity = int(input("Enter quantity: "))

    result = shop.calculate_bill(product, quantity)

    if isinstance(result, str):
        print(result)
    else:
        total, discount, final_amount = result

        print("Item Cost: Rs.", total)
        print("Discount: Rs.", discount)
        print("Final Amount: Rs.", final_amount)

        total_bill += total
        total_discount += discount

print("\n----- FINAL BILL -----")
print("Total Cost: Rs.", total_bill)
print("Total Discount: Rs.", total_discount)
print("Final Amount: Rs.", total_bill - total_discount)
print("Thank you for shopping!")