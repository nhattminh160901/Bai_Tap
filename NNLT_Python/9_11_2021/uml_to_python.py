class Item:
    def __init__(self, shippingWeight, description:str):
        self.shippingWeight = shippingWeight
        self.description = description
    
    def getPriceForQuantity(self):
        pass

    def getTax(self):
        pass

    def inStock(self):
        pass
    

class OrderDetails(Item):
    def add(self, quantity, taxStatus:str):
        self.quantity = quantity
        self.taxStatus = taxStatus

    def calcSubTotal(self):
        pass

    def calcWeight(self):
        pass

    def calcTax(self):
        pass

class Order:
    def __init__(self, date, status:str, s_o: OrderDetails): 
        self.date = date
        self.status = status
        self.s_o = s_o
    def calcSubTotal(self):
        return self.s_o.calcSubTotal()

    def calcTax(self):
        return self.s_o.calcTax

    def Total(self):
        pass

    def calcTotalWeight(self):
        pass

class Customer:
    def __init__(self, name:str, address):
        self.name = name
        self.address = address

class Payment:
    def __init__(self, amount:float):
        self.amount = amount        

class Cash(Payment):
    def add(self, cashTendered:float):
        self.cashTendered = cashTendered

class Check(Payment):
    def add(self, name:str, bankID:str):
        self.name = name
        self.bankID = bankID

    def authorized():
        pass

class Credit(Payment):
    def add(self, number:str, type:str, expDate):
        self.number = number
        self.type = type
        self.expDate = expDate
    
    def authorized():
        pass