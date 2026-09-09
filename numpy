import numpy as np

sales = np.array([1200, 2500, 1800, 3200, 4500, 2100, 1500])

# 1. Find the average of sales
print(np.mean(sales))

# 2. Find the maximum and minimum sales above 2000
print(np.max(sales[sales > 2000]))
print(np.min(sales[sales > 2000]))

# 3. Find values between 70 and 90
marks = np.array([65, 72, 85, 91, 78, 68, 88])

h_l = marks[(marks > 70) & (marks < 90)]
print(h_l)

# 4. Find sales below 1500 OR above 3000
lg = sales[(sales < 1500) | (sales > 3000)]
print(lg)

# 5. Calculate total sales between 2000 and 4000
total = np.sum(sales[(sales > 2000) & (sales < 4000)])
print(total)
