import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3

symbol_count = {
    "A" : 3,
    "B" : 3,
    "C" : 5,
    "D" : 4,
}

symbol_value = {
    "A" : 3,
    "B" : 4,
    "C" : 5,
    "D" : 3,
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = columns[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append[line+1]
    return winnings, winning_lines



def slot_machine_spin(rows,cols,symbols):
    all_symbol = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns 

def print_slot_machine(columns):
    for row in range(len(columns)):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ") 
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Please Enter the amount: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter the value greater than 0 ")
        else:
            print("Enter the valid amount")
    return amount

def get_lines_to_bet():
    while True:
        lines = input("Enter the lines to bet: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter the lines between 1 - {MAX_LINES}")
        else:
            print("Please enter the valid number of lines")
    return lines

def bet():
    while True:
        bet_amount = input("Enter the amount you wanna bet: ")
        if bet_amount.isdigit:
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"The bet amount should be between {MIN_BET} TO {MAX_BET}")
        else:
            print("Enter the valid amount!!")
    return bet_amount


def game(balance):
    lines = get_lines_to_bet()
    while True:
        bet_amount = bet()
        total_bet = lines * bet_amount
        if total_bet < balance:
            break
        else:
            print("Your bet amount has exceeded your balance")
    print(f"The balanace is {balance}\nThe number of lines are {lines}\nThe bet amount is {bet_amount}\nThe total bet is {total_bet}")
    slots = slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet_amount,symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet
        



def main():
    balance = deposit()
    while True:
        print(f"The current balance is {balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += game(balance)
    print(f"You left with {balance}")


main()
        