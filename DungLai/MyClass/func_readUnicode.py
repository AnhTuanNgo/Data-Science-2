import os

def func_covert_uf8_into_VietNames():
    "Tạo 2 list chứa ký tự tiếng việt và unicodes từ file txt"
    chars =[]
    unicodes =[]    
    path = os.getcwd()+"\\MyClass\\unicode.txt"
    file = open(path, encoding= "utf8")  #"unicode.txt"  
    table_uncode = file.read().split("\n")
    table_uncode = [f.split(" ") for f in table_uncode] #\t
    for li in table_uncode:
        chars.append(li[0])
        unicodes.append(li[1])
    # table_uncode = file.read().split("\r") # "\t" :tab
    return chars, unicodes

# Tìm chuỗi sau 2 ký tự đặc biệt
def func_covert_numberChar_into_VietNames(in_Str, chrSpecials, number_get_str):
    "in_Str = 'PHẠM HO&#192;NG H\xc6\xaf\xc6\xa0NG &#193;I'"
    "doulbe_chrSpecial = '&#'"
    "number_str = 3, tức là muốm lấy số: 192 và 193 trong in_str "
    ">>> [192, 193]"

    len_chrSpecials = len(chrSpecials) # chiều dài 
    
    for i, s in enumerate(in_Str):
        step = i + len_chrSpecials #i + 2
        if in_Str[i: step] == chrSpecials: #in_Str[i:i + 2]
            begin = step 
            after = begin + number_get_str
            in_Str = in_Str[:i] + chr(int(in_Str[begin:after])) + in_Str[after+1:]#[i+3:i+5]
            # in_Str[:i] là vị trí đang xét
            # in_Str[begin:after] là các số 192,193
            # in_Str[after+1:] là vị trí lấy đằng sau after 1 đơn vị

    return in_Str