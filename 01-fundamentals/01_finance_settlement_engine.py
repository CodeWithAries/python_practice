
# financesettlement engine

monthlySalary = float(input("Enter Monthly Salary     : "))
frelanceIncome =float(input("Enter Freelance Income   : "))
otherIncome =   float(input("Enter Other Income       : "))
print()

foodExpenses = float(input("Enter Food Expenses         : "))
transopoExpenses = float(input("Enter Transpo Expenses      : "))
housingExpenses = float(input("Enter Housing Expenses      : "))
utilityExpenses = float(input("Enter Utility Expenses      : "))
otherExpenses = float(input("Enter Other Expenses        : "))
print()

debtBalance = float(input("Emter Original debt Balance     : "))
interestRate = float(input("Enter Annual Interest Rate (%)  : "))
principalPayment = float(input("Enter Principal Payment         : "))
feeRate = float(input("Enter Processing fee rate (%)   : "))
print()
savingAllocation = float(input("Enter Savings allocation rate(%): "))
print()


total_income = monthlySalary + frelanceIncome + otherIncome
total_expenses = foodExpenses + transopoExpenses + housingExpenses + utilityExpenses + otherExpenses
debt_interest = debtBalance * (interestRate/100) * (1/12)
debt_settlement = principalPayment * (feeRate / 100)

total_debt_settlement = principalPayment + debt_interest + debt_settlement

remaining_balance = total_income - total_expenses - total_debt_settlement - 25

saving_allocation = remaining_balance * (savingAllocation/100)
final_available_cash = remaining_balance - saving_allocation

print("=========FINANCIAL REPORT===========\n")
print(f"Total Income: P{total_income:.2f}")
print(f"Total Expenses: P{total_expenses:.2f}")
print(f"Monthly Debt Interest: P{debt_interest:.2f}")
print(f"Debt Processing Fee: P{debt_settlement:2f} ")
print(f"Total Debt Settlement: P{total_debt_settlement:.2f}")
print(f"Transaction Fee: P{feeRate:.2f} ")
print("-----------------------------------\n")
print(f"Balance Before Savings:{remaining_balance:.2f}")
print(f"Saving Allocation: P{saving_allocation:.2f}")
print(f"Final Available Cash: P{final_available_cash:.2f}")




