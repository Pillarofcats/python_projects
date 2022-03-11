class Category:
  
  def __init__(self, category):
    #Variable/Definitions
    categories = ["Food", "Clothing", "Auto"]
    self.ledger = list()
    self.funds = 0
    self.balance = 0
    self.withdraw_total = 0
    #Check Category argument and assign index value
    category_index = categories.index(category)
    #Assign object Category attribute category
    self.category = categories[category_index]
    
  def __str__(self):
    title = f"*************{self.category}*************"
    category_len = len(self.category)
    title_len = 26 + category_len
    char_diff = abs(title_len - 30)
    if title_len > 30:
      for ch in range(char_diff):
        if ch % 2 == 0:
          title = title[:-1]
        else:
          title = title[1:]

    temp_ledger = []
    ledger_items = ""
    ledger_final = ""
    for item in self.ledger:
      amount = str(item["amount"])
      ledger_items = "{:<23} {:>6}".format(item["description"][:23], amount[:6])
      temp_ledger.append(ledger_items)
      ledger_final += ledger_items + "\n"

    total = "Total: {}".format(str(self.balance))

    return "{}\n{:<5}{}".format(title, ledger_final, total)


  def deposit(self, amount, description = None):
    if description == None:
      description = ""
    if amount < 0:
      amount = 0

    #format {"amount": amount, "description": description}
    self.ledger.append({"amount": amount, "description": description})
    self.funds += amount
    # self.balance = self.funds

    print(self.category,":","Deposited", amount)

  def withdraw(self, amount, description = None):
    #Use check_funds method
    if description == None:
      description = ""

    #Withdrawl did take place
    if self.check_funds(amount):
      #format {"amount": amount, "description": description}
      self.ledger.append({"amount": amount*(-1), "description": description})
      self.withdraw_total += amount
      print(self.category,":", "Withdrew", amount)
      print("Ledger:\n", self.ledger)
      self.get_balance()
      return True

    #Withdrawl did NOT take place
    else:
      print(self.category,":", "Can't withdrawl funds, not enough.")
      return False

  def get_balance(self):
    total_balance = 0
    for item in self.ledger:
      total_balance += item["amount"]
    self.balance = total_balance
    return "Checking Balance.."

  def transfer(self, amount, obj):
    #User check_funds method
    if self.check_funds(amount):

      description = "Transfer to " + obj.category
      self.withdraw(amount, description)

      description = "Transfer from " + self.category
      obj.deposit(amount, description)
      self.get_balance()
      return True

    else:
      return False

  def check_funds(self, amount):
    self.get_balance()
    if amount > self.balance:
      return False
    else:
      return True

def create_spend_chart(categories):

  #Calculate percentage spent for each category

  food_spent = int((categories[0].withdraw_total / categories[0].funds) * 100)
  clothing_spent = int((categories[1].withdraw_total / categories[1].funds) * 100)
  auto_spent = int((categories[2].withdraw_total / categories[2].funds) * 100)

  #Calculate percent values rounding down to the nearest 10th
  r_food_spent = round(food_spent/10)*10
  r_clothing_spent = round(clothing_spent/10)*10
  r_auto_spent = round(auto_spent/10)*10

  #Quadrant reference for 'o' values
  #[0][1] [0][2] [0][3]
  #[1][1] [1][2] [1][3]
  #[2][1] [2][2] [2][3]
  #[3][1] [3][2] [3][3]
  #[4][1] [4][2] [4][3]
  #[5][1] [5][2] [5][3]
  #[6][1] [6][2] [6][3]
  #[7][1] [7][2] [7][3]
  #[8][1] [8][2] [8][3]
  #[9][1] [9][2] [9][3]

  #Tables Keys/Titles
  percentages = [["100|"," ", " ", " "],
                 ["90|"," ", " ", " "],
                 ["80|", " ", " ", " "],
                 ["70|", " ", " ", " "],
                 ["60|", " ", " ", " "],
                 ["50|", " ", " ", " "],
                 ["40|", " ", " ", " "],
                 ["30|", " ", " ", " "],
                 ["20|", " ", " ", " "],
                 ["10|", " ", " ", " "],
                 ["0|", " ", " ", " "]]
  
  keys = [[" ", "F", "C", "A"],
          [" ", "o", "l", "u"],
          [" ", "o", "o", "t"],
          [" ", "d", "t", "o"],
          [" ", " ", "h", " "],
          [" ", " ", "i", " "],
          [" ", " ", "n", " "],
          [" ", " ", "g", " "]]

  #Determine bar chart values with 'o'
  for index in percentages:
    if r_food_spent >= int(index[0][0:-1]):
      index[1] = 'o'

    if r_clothing_spent >= int(index[0][0:-1]):
      index[2] = 'o'

    if r_auto_spent >= int(index[0][0:-1]):
      index[3] = 'o'

  #Print out bar chart
  print("Percentage spent by category")

  for row in percentages:
    print("{:>4s} {:^2s} {:^2s} {:^2s}".format(*row))

  print('{0:>14s}'.format('----------'))

  for row in keys:
    print("{:>4s} {:^2s} {:^2s} {:^2s}".format(*row))