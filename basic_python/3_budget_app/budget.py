class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.balance = 0
    self.withdrawals = 0

  def deposit(self, amount, description=""):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.balance -= amount
      self.withdrawals += amount
      self.ledger.append({"amount": -1*amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.withdraw(amount, f'Transfer to {category.name}'):
      category.deposit(amount, f'Transfer from {self.name}')
      return True
    else:
      return False

  def check_funds(self, amount):
    return False if amount > self.balance else True

  def __str__ (self):
    output = ""
    count = 30 - len(self.name)
    for _ in range(0, count // 2):
      output += "*"
    output += f'{self.name}'    
    for _ in range(0, (count // 2 if count % 2 == 0 else (count // 2) + 1 )):
      output += "*"
    for i in range(0, len(self.ledger)):
      description = self.ledger[i]["description"][:23]
      amount = format(float(self.ledger[i]["amount"]),".2f")
      spaces = 30 - (len(description) + len(amount))
      output += f'\n{description}'
      for _ in range(0, spaces):
        output += " "
      output += f'{amount}'
    output += f'\nTotal: {format(float(self.balance), ".2f")}'
    return output

def create_spend_chart(categories):
  withdrawals = list(map(lambda category: category.withdrawals, categories))
  max_length = max(list(map(lambda category: len(category.name), categories)))
  total = sum(withdrawals)
  percentages = list(map(lambda withdraw: ( (withdraw*100/total) / 10) * 10, withdrawals))
  chart = "Percentage spent by category\n"
  for i in range(100, -1, -10):
    for _ in range(0, 3 - len(str(i))):
      chart += " "
    chart += f'{i}|'
    for j in range(0, len(categories)):
      chart += " "
      chart += " " if percentages[j] < i else "o"
      chart += " "
    chart += " \n"
  chart += "    "
  for _ in range(0, len(categories)):
    chart += "---"
  chart += "-"
  for i in range(0, max_length):
    chart += "\n    "
    for j in range(0, len(categories)):
      chart += " "
      chart += categories[j].name[i] if len(categories[j].name) > i else " "
      chart += " "
    chart += " "
  return chart