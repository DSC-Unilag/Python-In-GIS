total_budget = int(input('Enter the amount budgeted for this month: >>>  '))
spent = 0
while True:
    amt = int(input('Enter expense: >> '))
    spent += amt
    cnt = input('do you want to continue? (y/n)')
    if cnt.lower()=='n': break
if spent > total_budget: print(f"You've spennt {spent-total_budget} more than your total budget")
else: print(f"You've spennt {total_budget - spent} less than your total budget")