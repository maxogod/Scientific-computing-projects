class Category:
    
    def __init__(self, category_name) -> None:
        self.ledger = []
        self.name = category_name
        
    def __str__(self) -> str:
        title = "*"*((30 - len(self.name))//2) + self.name + "*"*((30 - len(self.name))//2) + "\n"
        ledger_info = ""
        total = self.get_balance()
        for obj in self.ledger:
            if len(obj["description"]) > 23:
                ledger_info += obj["description"][:23]
            else:
                ledger_info += obj["description"].ljust(23)
            ledger_info += ("{:.2f}".format(obj["amount"])).rjust(7)
            ledger_info += "\n"
        ledger_info += "Total:" + ("{:.2f}".format(total)).rjust(7)
        return title + ledger_info
    
    def deposit(self, amount, description=""):
        """
        appends an object to the ledger list in the form 
        {"amount": amount, "description": description}
        """
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description="") -> bool:
        """
        appends an object to the ledger list in the form 
        {"amount": (-)amount, "description": description}
        if there are enough funds.
        returns whether the withdrawal was made or not.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        """
        returns current balance of the budget category.
        """
        balance = 0
        for obj in self.ledger:
            balance += obj["amount"]
        return balance
    
    def transfer(self, amount, scnd_budget_category) -> bool:
        if self.withdraw(amount, f"Transfer to {scnd_budget_category.name}"):
            scnd_budget_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount) -> bool:
        return self.get_balance() >= amount


def create_spend_chart(categories):
    pass
