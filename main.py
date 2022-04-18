class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = (self.name.rjust(15 + (len(self.name) // 2), '*')).ljust(30, '*') + '\n'
        descr = ''
        total = 0

        for item in self.ledger:
            a = item['description'][0:23]
            b = ("%.2f" % item['amount'])
            descr += item['description'][0:23] + b.rjust(30 - len(a)) + '\n'
            total += item['amount']

        return title + descr + 'Total: ' + str(total)

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        sum_balans = 0
        for item in self.ledger:
            sum_balans += item["amount"]
        return sum_balans

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + self.name)
            return True
        return False


#########################################################################################
def create_spend_chart(categories):
    sum_wihtdraw_all = 0
    sum_wihtdraw = {}
    percentage_categories = {}
    for categorie in categories:
        sum_wihtdraw[categorie.name] = 0
        percentage_categories[categorie.name] = 0

        for item in categorie.ledger:
            if item['amount'] < 0:
                sum_wihtdraw[categorie.name] += item['amount']
                sum_wihtdraw_all += item['amount']

    lenght = ''
    y = 0
    for c in sum_wihtdraw:
        if len(c) > len(lenght):
            lenght = c
            y = len(lenght)

        percentage_categories[c] = sum_wihtdraw[c] / sum_wihtdraw_all * 100
    line = len(categories) * 2 + len(categories) + 1
    output = "Percentage spent by category\n"
    i = 110
    count = float(100)

    for _ in range(11):
        i -= 10
        n = str(i).rjust(3)
        count1 = 0
        lst = ''
        while count1 < len(categories):
            if count <= percentage_categories[categories[count1].name]:
                lst += 'o  '
            else:
                lst += '   '
            count1 += 1

        output += n + "| " + lst + '\n'
        count -= 10
    output += ('-' * line).rjust(line + 4) + '\n'

    for j in range(y):
        count1 = 0
        lst1 = ''
        while count1 < len(categories):
            if len(categories[count1].name) > j:
                lst1 += categories[count1].name[j] + '  '
            else:
                lst1 += "   "

            count1 += 1
        if j != y - 1:

            output += "     " + lst1 + "\n"
        else:

            output += "     " + lst1

    # print(percentage_categories)
    return output


# Starter code by nik

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
# print(create_spend_chart([food, clothing, auto]))
business = Category('Business')
food = Category('Food')
food.deposit(900, "deposit")
entertainment = Category('Entertainment')
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))
