
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
    
    
    def category_name(self):
        return self.name
    
    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total

def create_spend_chart(categories):
    percentages = []
    total_withdrawals = 0
    for category in categories:
        total_withdrawals += category.get_withdrawals()
    for category in categories:
        percentages.append((category.category_name(), int(round(category.get_withdrawals() * 100 / total_withdrawals))))
    
    strin = "Percentage spent by category\n"
    i = 100
    while i >= 0:
        for j in range(len(categories)):
            if j == 0:
                if percentages[j][1] >= i:
                    strin += f"{str(i).rjust(3)}| o"
                else:
                    strin += f"{str(i).rjust(3)}|  "
            elif j == len(categories) - 1:
                if percentages[j][1] >= i:
                    strin += f"  o  \n"
                else:
                    strin += f"     \n"
            else:
                if percentages[j][1] >= i:
                    strin += f"  o"
                else:
                    strin += f"   "
        i -= 10
                
    strin += "    " + "-".ljust(3 * len(categories) + 1, "-") + "\n"
    
    max_len = max(len(categories[index].category_name()) for index in range(len(categories)))
    i = 0
    while i < max_len:
        for j in range(len(categories)):
            if j == 0:
                try:
                    strin += f"     {(categories[j].category_name())[i]}"
                except IndexError:
                    strin += f"      "
            elif j == len(categories) - 1:
                try:
                    strin += f"  {(categories[j].category_name())[i]}  \n"
                except IndexError:
                    strin += f"     \n"
            else:
                try:
                    strin += f"  {(categories[j].category_name())[i]}"
                except IndexError:
                    strin += f"   "
        i += 1
            
    return strin[:-1]
