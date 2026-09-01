expenses = [1200,1300,1400,1500]
total_expenses = 0
for i in range (len(expenses)):
    expense = expenses[i]
    print(f"month {i+1}, expense: {expense}")
total_expenses +=expense
print("total",total_expenses)