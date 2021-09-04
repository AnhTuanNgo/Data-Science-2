import numpy as np
import pandas as pd

"Khai báo random cho giá trị giống nhau trên tất cả các máy tính"
np.random.seed(0)

# Tạo ma trận (5,3) với số lượng bán từng món là các phần tử cho random từ 0-20
sales_amounts = np.random.randint(20, size=(5,3))
print(sales_amounts)

# Tạo DataFrame với pandas:
weekly_sales = pd.DataFrame(sales_amounts, index=['Mon', 'Tue', 'Wed', 'Thurs', 'Fri'], columns=['Chicken', 'Pig', 'Beef'])

prices = np.array([10, 8, 12]).reshape(1,3)
# prices = prices.T
sales_price = pd.DataFrame(prices, index=['Price'], columns=['Chicken', 'Pig', 'Beef'])

# Ma trận đảo (3,1)
sales_price = sales_price.T
# print('sales_price', sales_price)

sum_Matric = weekly_sales.dot(sales_price)
print('sales_price', sum_Matric)
"""Giải thích tích vô hướng 2 vector weekly_sales.dot(sales_price):
Giá trị 240: 12*10+15*8+0*12
Giá trị 138: 3*10+3*8+7*12
...
"""

# Đưa cột tổng vào DataFrame
weekly_sales["Total prices"] = sum_Matric

print('weekly_sales', weekly_sales)





