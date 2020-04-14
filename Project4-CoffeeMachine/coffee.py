class CoffeeMachine():
    def __init__(self):
        self.cashBox = CashBox()
        self.selector = Selector(self.cashBox)

    def oneAction(self):
        while(True):
            print("PRODUCT LIST: all 35 cents, except bouillon (25 cents)")
            print("1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon")
            print("Sample commands: insert 25, select 1.\n")
            command = input("Your Command: ").lower().split()

            if command[0] == "insert" and len(command) > 1:
                #call cashBox and let it do all the work
                self.cashBox.deposit(int(command[1]))
            elif command[0] == "select" and len(command) > 1:
                #call selector and let it do all the work
                self.selector.select(int(command[1]))
            elif command[0] == "cancel" :
                #return any money already deposited
                self.cashBox.returnCoins()
            elif command[0] == "quit":
                #return any money already deposited
                return False
            else:
                #Error, invalid command, priint message for user
                print("\nInvalid command\n")


    def totalCash(self):
        #output total cash
        return self.cashBox.total()
        

class CashBox():
    def __init__(self):
        self.credit = 0
        self.totalRecieved = 0.0

    def deposit(self, amount):
        if amount == 50 or amount == 25 or amount == 10 or amount == 5:
            self.credit += amount
            self.totalRecieved += amount
            print("\nDepositing " + str(amount) + " cents. You have " + str(self.credit) + " left.\n")
        else:
            print("\nWe only take half-dollars, quarters, dimes, and nickles.\n")
            self.credit += amount
            self.returnCoins()

    def returnCoins(self):
        print("\nReturning " + str(self.credit) + " cents.\n")
        self.totalRecieved -= self.credit
        self.credit = 0
        return self.credit
        

    def haveYou(self, amount):
        if amount <= self.credit:
            return True
        else:
            return False

    def deduct(self, amount):
        self.credit -= amount
        self.returnCoins()

    def total(self):
        return self.totalRecieved

class Selector():
    def __init__(self, cashBox):
        self.cashBox = cashBox
        self.products = []
        self.SetProducts()

    def SetProducts(self):
        self.products.append(Product("Black", 35, "Dispensing Cup\nDispensing Coffee\nDispensing Water"))
        self.products.append(Product("White", 35, "Dispensing Cup\nDispensing Coffee\nDispensing Cream\nDispensing Water"))
        self.products.append(Product("Sweet", 35, "Dispensing Cup\nDispensing Coffee\nDispensing Sugar\nDispensing Water"))
        self.products.append(Product("White & Sweet", 35, "Dispensing Cup\nDispensing Coffee\nDispensing Cream\nDispensing Sugar\nDispensing Water"))
        self.products.append(Product("Bouillon", 25, "Dispensing Cup\nDispensing bouillionPowders\nDispensing Water"))

    def select(self, index):
        if index > 5 or index <= 0:
            print("\nInvalid selection, please make a selection between 1-5\n")
        else:
            index -= 1
            selected = self.products[index]
            price = selected.getPrice()
            if self.cashBox.haveYou(price):
                print(selected.make())
                self.cashBox.deduct(price)
            else:
                print("\nThis item is ", price, "cents and you have a credit of: ", self.cashBox.credit,"cents \n")
        

class Product():
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def getPrice(self):
        return self.price

    def make(self):
        print("Making ",self.name, ":")
        return self.recipe

def main():
    m = CoffeeMachine()
    while m.oneAction():
        pass
    total = m.totalCash()
    print(f"\nTotal cash: ${total/100:.2f}")

if __name__ == "__main__":
    main()