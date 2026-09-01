monthly_sales = [42,38,33,38,40,45]
months = ["jan","feb","march","april","may","june"]
thresold = 35
for sales_amount,months in zip(monthly_sales,months):
    if sales_amount<thresold:
        print(f"sales amount {sales_amount} is less than threshold in {months} ")
        break
    else:
                print(f"sales amount {sales_amount} is greater than threshold in {months} ")


