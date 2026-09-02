# def sum_all(*args):
#     total = 0
#     for num in args:
# 	    total += num
#     return total

# total = sum_all(1,2,3,4)
# print(total)
def company_info(**kwargs):
	for key in kwargs:
		print(key,kwargs[key])

company_info(ricker = 'AAPL',ceo = 'Tim Cook', revenue = '200 billion', pe = 20, pb = 10.2)