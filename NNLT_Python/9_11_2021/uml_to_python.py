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
    def __init__(self, shippingWeight, description:str, quantity, taxStatus:str):
        super().__init__(shippingWeight, description)
        self.quantity = quantity
        self.taxStatus = taxStatus

    def calcSubTotal(self):
        pass

    def calcWeight(self):
        pass

    def calcTax(self):
        pass

class Order:
    def __init__(self, date, status:str): 
        self.date = date
        self.status = status
        self.s_o = OrderDetails
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
    def __init__(self, amount:float, cashTendered:float):
        super().__init__(amount)
        self.cashTendered = cashTendered

class Check(Payment):
    def __init__(self, amount:float, name:str, bankID:str):
        super().__init__(amount)
        self.name = name
        self.bankID = bankID

    def authorized():
        pass

class Credit(Payment):
    def __init__(self, amount:float, number:str, type:str, expDate):
        super().__init__(amount)
        self.number = number
        self.type = type
        self.expDate = expDate
    
    def authorized():
        pass