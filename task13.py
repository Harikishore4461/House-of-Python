class CoffeeMachine:
    def __init__(self):
        print("Coffee machine is ON")
        self.water = 2000
        self.milk = 1500
        self.coffee = 1000
        self.money = 10

    def report(self):
        print("The Current resource Available are:")
        print("Water : ", self.water)
        print("Milk  : ", self.milk)
        print("Coffee: ", self.coffee)
        print("Money : ", self.money)

    def checkResources(self, coffee):
        if coffee["milk"] >= self.milk:
            print("Sorry there is not enough Milk")
            return -1
        elif coffee["water"] >= self.water:
            print("Sorry there is not enough Water")
            return -1
        elif coffee["coffee"] >= self.coffee:
            print("Sorry there is not enough Coffee")
            return -1
        else:
            return 1

    def getMoney(self):
        print("Insert Coins")
        q = int(input("Enter no.of Quarters: "))
        d = int(input("Enter no.of Dimes: "))
        n = int(input("Enter no.of Nickel: "))
        p = int(input("Enter no.of Pennies: "))

        return (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)

    def checkMoney(self, coffee, amount):
        if coffee["money"] > amount:
            print("\nSorry that's not enough money")
            return -1
        elif coffee["money"] < amount:
            self.money = self.money + coffee["money"]
            self.water = self.water - coffee["water"]
            self.milk = self.milk - coffee["milk"]
            self.coffee = self.coffee - coffee["coffee"]
            print("\n---->Here is the change: ", amount - coffee["money"])
            return 1
        else:
            self.money = self.money + coffee["money"]
            self.money = self.money + coffee["money"]
            self.water = self.water - coffee["water"]
            self.milk = self.milk - coffee["milk"]
            self.coffee = self.coffee - coffee["coffee"]
            return 1


if __name__ == "__main__":
    CoffeeClass = CoffeeMachine()
    print("Welcome To Coffee Shop")
    print("Select the coffe: \n1)Latte\t2)Cappuccino\t3)Expresso\t4)Off\t5)Report")
    latte = {"water": 200, "milk": 150, "coffee": 25, "money": 5}
    cappuccino = {"water": 100, "milk": 150, "coffee": 30, "money": 7}
    expresso = {"water": 100, "milk": 100, "coffee": 40, "money": 10}

    while True:
        n = str(input("Enter the coffe number or any other options: ")).lower()

        if n == "report":
            CoffeeClass.report()

        elif n == "latte":
            flag = CoffeeClass.checkResources(latte)
            if flag == -1:
                break
            amount = CoffeeClass.getMoney()
            flag = CoffeeClass.checkMoney(latte, amount)
            if flag == -1:
                break
            print("\n--->Here is Your Latte. Enjoy!")
            CoffeeClass.report()


        elif n == "cappuccino":
            flag = CoffeeClass.checkResources(cappuccino)
            if flag == -1:
                break
            amount = CoffeeClass.getMoney()
            flag = CoffeeClass.checkMoney(cappuccino, amount)
            if flag == -1:
                break
            print("\n--->Here is Your Cappuccino. Enjoy!")
            CoffeeClass.report()

        elif n == "expresso":
            flag = CoffeeClass.checkResources(expresso)
            if flag == -1:
                break
            amount = CoffeeClass.getMoney()
            flag = CoffeeClass.checkMoney(expresso, amount)
            if flag == -1:
                break
            print("\n--->Here is Your Expresso. Enjoy!")
            CoffeeClass.report()

        elif n == "off":
            break

    print("Coffee Machine is Turning OFF")