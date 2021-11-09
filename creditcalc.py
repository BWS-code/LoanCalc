import math
import argparse
import sys


def n_mode(loan_principal, monthly, loan_interest):
    i = loan_interest / (12 * 100)
    months = round_up(math.log(monthly / (monthly - i * loan_principal), 1 + i))
    over = int(monthly * months - loan_principal)
    years = f"{months // 12} year{'s'[:months // 12 ^ 1]}" if months // 12 else ''
    months = f"{months % 12} month{'s'[:months % 12 ^ 1]}" if months % 12 else ''
    _and_ = ' and ' if years and months else ''
    print(f"It will take {years}{_and_}{months} to repay this loan!")
    print(f"Overpayment = {round_up(over)}")


def a_mode(loan_principal, months, loan_interest):
    i = loan_interest / (12 * 100)
    monthly = loan_principal * (i * (1 + i) ** months / ((1 + i) ** months - 1))
    over = (round_up(monthly) - (loan_principal / months)) * months
    print(f"Your monthly payment = {round_up(monthly)}!")
    print(f"Overpayment = {round_up(over)}")


def p_mode(monthly, months, loan_interest):
    i = loan_interest / (12 * 100)
    loan_principal = int(monthly / (i * (1 + i) ** months / ((1 + i) ** months - 1)))
    over = int(monthly * months - loan_principal)
    print(f"Your loan principal = {loan_principal}!")
    print(f"Overpayment = {over}")


def d_mode(loan_principal, months, loan_interest, over=0):
    i = loan_interest / (12 * 100)
    for m in range(months):
        monthly = loan_principal / months + (i * (loan_principal - (loan_principal * m / months)))
        print(f"Month {m + 1}: payment is {round_up(monthly)}")
        over += round_up(monthly) - int(loan_principal / months)
    print(f"Overpayment = {over}")


def round_up(what):
    return int(what) if not what - int(what) else int(what) + 1


def main():
    print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal,
type "d" for differentiated payments:''')
    mode = input()
    if mode == 'n':
        n_mode(*map(float, (
            input('Enter the loan principal:'),
            input('Enter the monthly payment:'),
            input('Enter the loan interest:'))))
    if mode == 'a':
        a_mode(*map(float, (
            input('Enter the loan principal:'),
            input('Enter the number of periods:'),
            input('Enter the loan interest:'))))
    if mode == 'p':
        p_mode(*map(float, (
            input('Enter the annuity payment:'),
            input('Enter the number of periods:'),
            input('Enter the loan interest:'))))
    if mode == 'd':
        d_mode(*map(float, (
            input('Enter the loan principal:'),
            input('Enter the number of periods:'),
            input('Enter the loan interest:'))))


if len(sys.argv) == 1:
    main()

parser = argparse.ArgumentParser(description='')
parser.add_argument('-typ', '--type')
parser.add_argument('-pay', '--payment', type=float)
parser.add_argument('-pri', '--principal', type=float)
parser.add_argument('-per', '--periods', type=int)
parser.add_argument('-int', '--interest', type=float)

args = parser.parse_args()

if \
        not args.type or \
        not args.interest or \
        args.type not in ('annuity', 'diff') or \
        args.type == 'diff' and args.payment or \
        list(vars(args).values()).count(None) > 1 or \
        list(x for x in list(vars(args).values())[1:] if x and x < 0):
    print('Incorrect parameters')
else:
    if args.type == 'annuity':
        mode = ''.join(k for k, v in vars(args).items() if not v)
        if mode == 'periods':
            n_mode(args.principal, args.payment, args.interest)
        if mode == 'payment':
            a_mode(args.principal, args.periods, args.interest)
        if mode == 'principal':
            p_mode(args.payment, args.periods, args.interest)
    if args.type == 'diff':
        d_mode(args.principal, args.periods, args.interest)
