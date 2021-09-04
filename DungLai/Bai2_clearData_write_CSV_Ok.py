# import subprocess
# result = subprocess.check_output('curl  -F"sobaodanh=02000001" diemthi.hcm.edu.vn/Home/Show')
# print(result)
import csv
import timeit as ti
from MyClass.func_data_Science import *

from MyClass.func_readUnicode import *

fisrt_time= ti.default_timer()
# Gán biến chars, unicodes để tiếp tục xử lý thông tin 
chars, unicodes = func_covert_uf8_into_VietNames()
# print(chars, unicodes)


# Bài 2_3: Làm sạch dữ liệu dòng đầu tiên của file txt:
read_file = open("raw_data_Dung.txt", "r")
# new_text = open("test.txt", encoding="utf8", mode="w")

# Witer header to CSV

with open("cleanData20210728.csv", encoding="utf8", mode="w", newline='') as file_csv:
    header = ['sbd','tên', 'ngày', 'tháng', 'năm','toán', 'ngữ văn', 'ktxh', 'khtn', 'lịch sử', 'địa lí', 'gdcd', 'sinh học', 'vật lí', 'hóa học', 'tiếng anh']
    writer = csv.writer(file_csv)
    writer.writerow(header)

read_rows = read_file.read().split("\n")
SBD = 2000000
for read_row in read_rows:
    try: 
        SBD += 1
        read_row = read_row.split("\\n")
        
        new_str =[]
        for s in read_row:    
            s = s.replace("\\r", "")    
            s = s.strip() #Xóa khoảng trống đầu cuối, kể cả dòng trống
            
            # Tạo 1 list chuỗi nằm trong "<sdfsdfsdfsdf>" 
            list_char = func_get_Str_between_two_specical("<", s, ">")
            for ch in list_char:
                s = s.replace(ch, "")
            if s!="":
                new_str.append(s)
        # new_text.write(line + "\n" for line in new_str )


        # print(new_text) # dòng thứ 8->10 cần dùng

        # Write dòng từ 8->10, với thứ tự index 7->9
        row_use=[]
        row_use.append(new_str[7])
        row_use.append(new_str[8])
        row_use.append(new_str[9])
        # print (new_str)

        for i, code in enumerate(unicodes):
            row_use[0] = row_use[0].replace(unicodes[i], chars[i])    
            row_use[1] = row_use[1].replace(unicodes[i], chars[i])
            row_use[2] = row_use[2].replace(unicodes[i], chars[i])

        # cover mã ACC thành tiếng việt dòng 0
        row_use[0] = func_covert_numberChar_into_VietNames(row_use[0],"&#",3)
        row_use[2] = func_covert_numberChar_into_VietNames(row_use[2],"&#",3)

        # In thuong hết dữ liệu
        row_use[0]=row_use[0].lower()
        row_use[1]=row_use[1].lower()
        row_use[2]=row_use[2].lower()

        # Tách ngày tháng năm
        row_use[1] = row_use[1].split("/")

        # Xử lý điểm thi
        row_use[2] = row_use[2].replace(":", "")
        row_use[2] = row_use[2].replace("khxh ", "ktxh   ")
        row_use[2] = row_use[2].replace("khtn ", "khtn   ")
        row_use[2] = row_use[2].split("   ")

        # Gán tên thành list
        names_list = row_use[0].title()
        birth_list = row_use[1]
        scores = row_use[2]   
        subject = ['toán', 'ngữ văn', 'ktxh', 'khtn','lịch sử', 'địa lí', 'gdcd', 'sinh học', 'vật lí', 'hóa học', 'tiếng anh']

        # id= func_num_ixdex_of_list(subject, 'ktxh')
        # id1 = func_num_ixdex_in_list(subject, 'lịch sử')
        data =[str(SBD), names_list, *birth_list]

        for sj in subject:
            if sj in scores:
                data.append(scores[func_num_ixdex_in_list(scores, sj)+1]) #score_list.append(scores[scores.index(sj)+1])
            else:
                data.append('-1')
                # score_list.append(str(float(row_use[2][row_use[2].index+1])))

        # print(data)
        
        # # ghi ra file txt
        # new_text = open("test.txt", encoding="utf8", mode="a")
        # for row in data:
        #     new_text.write(row +",")

        # new_text.write('\n')

        # ghi ra file csv
        with open("cleanData20210728.csv", "a", encoding="utf8", newline='') as file_csv:
            # for row in data:
            writer = csv.writer(file_csv)
            writer.writerow(data)

    except:
        continue
print("Witer CSV successfull !!!!!")
end_time= ti.default_timer()
print(end_time - fisrt_time)