# import subprocess
# result = subprocess.check_output('curl  -F"sobaodanh=02000001" diemthi.hcm.edu.vn/Home/Show')
# print(result)

#Lọc chuỗi giữa 2 ký tự:
def get_Str_between_two_specical( chr1, in_str, chr2):
    str_out =[]
    for i, s in enumerate(in_str):
        if s==chr1:
            begin=i
        elif s==chr2:
            after=i+1
            str_out.append(in_str[begin:after])
    return str_out

# Bài 2_3: Làm sạch dữ liệu:
read_file = open("raw_data_Dung.txt", "r")
read_row = read_file.readline()
read_row = read_row.split("\\n")


new_text = open("test.txt", "w")
new_str =[]
for s in read_row:
    if s != "":    
        s = s.replace("\\r", "")
        s = s.replace("\\t", "")
        s = s.replace(" ", "")
        s = s.strip()
        
        # Tạo 1 list chuỗi nằm trong "<sdfsdfsdfsdf>" 
        list_char = get_Str_between_two_specical( "<", s, ">")
        for ch in list_char:
            s = s.replace(ch, "")
        new_str.append(s)
new_text.write(line + "\n" for line in new_str )
    