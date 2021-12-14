loan_p = input('Enter the loan principal:\n')
mode = input('What do you want to calculate?\n\
type "m" - for number of monthly payments,\n\
type "p" - for the monthly payment:\n')
entry = input('Enter the number of months:\n') if mode == 'p' else \
            input('Enter the monthly payment:\n')

loan_p, entry = map(int, (loan_p, entry))
per_or_pay = loan_p // entry + 1 if loan_p / entry - loan_p // entry else loan_p // entry

if mode == 'm':
    print('It will take {} month{} to repay the loan'.format(per_or_pay, 's' if per_or_pay > 1 else ''))
if mode == 'p':
    last_one = loan_p % per_or_pay or ''
    print('Your monthly payment %s %s%s' % (per_or_pay, 'and the last payment = ' if last_one else '', last_one))
