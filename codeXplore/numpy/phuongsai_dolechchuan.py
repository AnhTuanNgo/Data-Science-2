import numpy as np

"Cách Standard and Variance: Phương sai và độ lệch chuẩn"
# https://www.youtube.com/watch?v=1eSmR2EJjYM, phút 50:00

"Cho chiều cao các con chó"
dog_hieght = [600, 470, 170, 430, 300]
dog_hieght = np.array(dog_hieght)
# print(dog_hieght)

"methol 1: Tính độ lệch chuẩn"
standard_hieght_1 = np.std(dog_hieght)
print("methol 1:", standard_hieght_1)

"methol 2: Tính độ lệch chuẩn"
# Phương sai độ lệch: Độ chênh lệch chiều cao so với chiều cao trung bình
var_hieght = np.var(dog_hieght)
standard_hieght_2 = np.sqrt(var_hieght)
print("methol 2:", standard_hieght_2)

"methol 3: ------------------Tính độ lệch chuẩn bằng thủ công để hiểu bài toán----------------"
# Chiều cao trung bình
mean_hieght = np.mean(dog_hieght)

# Phương sai: chênh lệch từng chiều cao từng con so với trung bình 
"Độ lệch so với chiều cao trung bình var_hieght_with_element = "
var_hieght_with_element=[]
for i_hieght in range(len(dog_hieght)):
    element_hiegh = dog_hieght[i_hieght] - mean_hieght
    var_hieght_with_element.append(element_hiegh)

# Bình phương khoàng cách chênh lệch (loại giá trị âm)
square_element =[]
for elm in var_hieght_with_element:
    sq = elm**2
    square_element.append(sq)
# phương sai: var^2 = sum(square_element)/element
var_hieght = np.sum(square_element)/len(square_element)
standard_hieght_3 = np.sqrt(var_hieght)
print("methol 3:", standard_hieght_3)
