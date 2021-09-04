import subprocess
result = subprocess.check_output('curl -F "Sobaodanh=02000001"  http://diemthi.hcm.edu.vn/Home/Show')#thay cho việc "C:\Users\Mr VU>curl -F "Sobaodanh=02074718"  http://diemthi.hcm.edu.vn/Home/Show"
print(result)
with open("data_Vu","w") as file:
file = open("data_Vu","w")#open("data_Vu","a"), "a": append thực hiện write thêm ko xóa dữ liệu cũ, ngược lại "w"
for i in range(10):
	file.write(str(i) + "\n")

file = open("data_Vu","r")
# read_file = file.read()# read cả file text, nếu muốn trả lại list thì dùng thêm split("\n")
read_file = file.read().split("\n")
# so sánh "file.read()" và "file.read().split("\n")": tìm và tách các ký tự xuống dòng 
print(read_file)
for i in range(len(read_file)):
	print(read_file[i])