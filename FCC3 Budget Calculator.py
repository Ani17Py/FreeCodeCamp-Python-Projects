class Category:
    def __init__(self, name):
        idd = str(name)
        self.name = name
        self.idd = idd
        self.ledger = []
        self.balance = 0
        leng = len(self.idd)
        self.leng = leng
        inw = 0
        wit = []
        self.inw = inw
        self.wit = wit

    def deposit(self, amt, desc=''):
        self.ledger.append({"amount": amt, "description": desc})
        self.balance += amt
        self.inw += amt

    def withdraw(self, wamt, wdesc=''):
        if wamt < self.balance:
            self.ledger.append({"amount": -wamt, "description": wdesc})
            self.balance -= wamt
            self.wit.append(wamt)
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amt, name1):
        if amt <= self.balance:
            self.withdraw(amt, f'Transfer to {name1.idd}')
            name1.deposit(amt, f'Transfer from {self.idd}')
            return True
        else:
            return False

    def check_funds(self, amt):
        return True if amt <= self.balance else False

    def __str__(self):
        orig = ''
        orig += '*' * (15 - int(self.leng / 2))
        orig += self.idd
        orig += '*' * (15 - int(self.leng / 2))
        i = 0
        for i in self.ledger:
            des = i['description']
            val = (str(i['amount']))
            val += '.00' if '.' not in val else ''
            des = des[0:30 - len(val) - 1]
            bal = str(self.balance)
            orig += '\n' + des + ' ' * int(30 - len(des) - len(val)) + val
        orig += '\n' + 'Total: ' + bal
        return orig.strip()


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
clothing.deposit(1000)
clothing.withdraw(400)
food.transfer(400, clothing)
auto = Category('Auto')
auto.deposit(100)
auto.withdraw(78)
business = Category('Business')
business.deposit(1000)
business.withdraw(600)


def create_spend_chart(categories=[]):
    dic = {}
    n = 100
    string = 'Percentage spent by category\n'.strip(' ')
    div = '    ' + '---' * len(categories) + '-'
    for cat in categories:
        dic[cat.idd] = sum(cat.wit)
    num = sum(dic.values())
    while n >= 0:
        spc = ''
        for val in dic:
            spc += ' o ' if (dic[val] / num * 100) >= n else '   '
        string += f"{n:>3}|{spc} \n"
        n -= 10
    string += div + '\n'
    names_cat = dic.keys()
    max_len = max(names_cat, key=len)
    for i in range(len(max_len)):
        spc_str = "    "
        for name in names_cat:
            spc_str += '   ' if i >= len(name) else f' {name[i]} '

        if i != len(max_len) - 1:
            spc_str += ' \n'

        string += spc_str

    return string + ' '


print(create_spend_chart([food, clothing, auto]))








