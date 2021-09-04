from numpy.core.function_base import linspace
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_cities = pd.read_csv("california_cities.csv")
# data_cities.head()
# print(data_cities.columns)

# I.Trang trí: 

# I.1 Phóng to bản đồ theo truc x, y dễ nhìn
plt.figure(figsize=(8,6))

# I.2 Chọn hình nền 
plt.style.use('seaborn')


# latd: vĩ độ, longd: kinh độ
lat, lon = data_cities['latd'], data_cities['longd']
pop, rea = data_cities['population_total'], data_cities['area_total_km2']
# Vẽ biểu đồ phân bố rời rạc
plt.scatter(lon, lat, c=np.log10(pop), cmap='viridis', s=rea, linewidths=1, alpha=0.5)
"Ghi chú: c: color, c=pop; quá to, giảm xuống c=np.log10(pop) "
"cmap='viridis' : tô cho có màu hơn"
"s: là scale Để thay đổi dấu tròn to, nhỏ theo tỷ lệ (rea)"
"linewidths: độ lan rộng của dấu tròn"

# Phân bố đều 2 trục
plt.axis('equal') 
plt.xlabel('longtitude: Kinh độ')
plt.ylabel('latitude: Vĩ độ')

# Thên bar màu cho cột
plt.colorbar(label='log$_{10}$(pop)')
# 'log$_{10}$: cách ghi chú cho log cơ số 10

# Giới hạn lại cột colorbar. settup từ 3-7 thay 0-7
plt.clim(3,7)

plt.title("Biểo đồ phân bố dân cư, diện tích California")

# Chú thích về bản đồ:
"In ra diện tích để chọn tỷ lệ phù hợp"
# print(data_cities['area_total_km2'].sort_values(ascending=False)) #1302.000, 964.510, 527.401,466.109,371.946 
# legend
area_range=[50, 100, 300, 500, 800, 1000]
for area in area_range:
    plt.scatter([], [], s= area, label= str(area) +'(Km$2$)')
    "s: scale tỉ lệ"

# Vẽ chú thích lên biểu đồ:
plt.legend(title = "Area")

plt.show() #map_cities.png
# print(lat, lon)