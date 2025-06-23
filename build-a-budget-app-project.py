** start of main.py **

class Category:
    def __init__(self, ledger):
        self.cat_name = str(ledger)
        self.ledger = []
        self.total_spent = 0

    def __str__(self):
        budget_print_string = ''
        for i in range((30 - len(self.cat_name))//2):
            budget_print_string += '*'
        budget_print_string += self.cat_name
        while len(budget_print_string) < 30:
            budget_print_string += '*'
        
        for entry in self.ledger:
            #formats the ledger string accordingly
            if len(entry['description']) > 23:
                budget_print_string += '\n' + entry['description'][:-(len(entry['description']) - 23)] + self.format_amount(entry['amount']).rjust(7, ' ')
            else: 
                budget_print_string += '\n' + entry['description'] + self.format_amount(entry['amount']).rjust(30 - len(entry['description']))

        return budget_print_string + '\nTotal: ' + self.format_amount(self.get_balance())

    #My crazy way of getting 2 decimal place formatting
    #Returns strings
    def format_amount(self, amount):
        amount_2dec = str(amount).split('.')[0]
        if len(str(amount).split('.')) > 1:
            amount_2dec += '.' + ((str(amount).split('.')[1]) + '00')[:2]
            return amount_2dec
        return amount_2dec + '.00'

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.total_spent += amount
            return True
        return False

    def get_balance(self):
        balance = 0
        for record in self.ledger:
            balance += record['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.cat_name}')
            category.deposit(amount, f'Transfer from {self.cat_name}')
            return True
        return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        return False

def create_spend_chart(categories):
    total_spent_all = 0
    percentage_spent = []
    spend_chart_string = f'Percentage spent by category\n'
    percent = 100
    for cat in categories:
        total_spent_all += cat.total_spent

    for cat in categories:
        percentage_spent.append((100*cat.total_spent)/total_spent_all)
    
    for i in range(11):
        spend_chart_string += str(percent).rjust(3) + '|'
        for value in percentage_spent:
            if value >= percent:
                spend_chart_string += ' o '
            
            else:
                spend_chart_string += '   '
        spend_chart_string += ' '
        spend_chart_string += '\n' 
        percent -= 10   
    spend_chart_string += '    '

    for i in range(len(categories)):
        spend_chart_string += '---'
    spend_chart_string += '-'

    #get max name length
    max_name_length = 0
    for i in categories:
        if len(str(i.cat_name)) > max_name_length:
            max_name_length = len(str(i.cat_name))
    
    
    for i in range(max_name_length):
        spend_chart_string += '\n     '
        for j in categories:
            if j.cat_name[i:i+1]:
                spend_chart_string += f'{j.cat_name[i:i+1]}  '
            else:
                spend_chart_string += '   '
        
    return spend_chart_string
    #return percentage_spent
    

sugar = Category('sugar')
sugar.deposit(100.01, 'for sweets')
sugar.deposit(100, 'for sweets')
sugar.deposit(10096.45, 'for sweets')
sugar.deposit(100, 'for sweets')
sugar.deposit(100, 'for sweets')
sugar.deposit(100, 'for sweets')
frog = Category('frog')
turtle = Category('turtle')
turtle.deposit(123, 'for shell')
turtle.withdraw(12, 'for beef')
beef = Category('beef')
snake = Category('snake')
frog.deposit(234, 'for legs')
frog.withdraw(188, 'spending')
beef.deposit(345, 'for horns')
snake.deposit(76767, 'for scales')
sugar.transfer(36, frog)
#print(sugar.get_balance(), frog.get_balance())
#print(sugar)

print(create_spend_chart([sugar, frog, beef, snake, turtle]))

** end of main.py **

