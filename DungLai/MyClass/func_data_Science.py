#Lọc chuỗi giữa 2 ký tự:
def func_get_Str_between_two_specical( chr1, in_str, chr2):
    "Tìm chuỗi nằm trong 2 ký tự đặc biệt"
    str_out =[]
    for i, s in enumerate(in_str):
        if s==chr1:
            begin=i
        elif s==chr2:
            after=i+1
            str_out.append(in_str[begin:after])
    return str_out

# Tìm chuỗi sau 2 ký tự đặc biệt
def func_find_str_after_two_chrSpecial(in_Str, chrSpecials, number_get_str):
    "in_Str = 'PHẠM HO&#192;NG H\xc6\xaf\xc6\xa0NG &#193;I'"
    "doulbe_chrSpecial = '&#'"
    "number_str = 3, tức là muốm lấy số: 192 và 193 trong in_str "
    ">>> [192, 193]"

    len_chrSpecials = len(chrSpecials) # chiều dài 
    out_str =[]
    for i, s in enumerate(in_Str):
        step = i + len_chrSpecials #i + 2
        if in_Str[i: step] == chrSpecials: #in_Str[i:i + 2]
            begin = step 
            after = begin + number_get_str
            out_str.append(in_Str[begin:after]) #[i+3:i+5]

    return out_str

# tìm vị trí phần tử trong list, index in list (cách 1)
def func_num_ixdex_in_list(into_list, value_inlist):
    # subject = ['toán', 'ngữ văn', 'ktxh', 'kttn','lịch sử', 'địa lí', 'gdcd', 'sinh học',  'tiếng anh']
    # id= func_num_ixdex_of_list(subject, 'ktxh')    
    return into_list.index(value_inlist)

# tìm vị trí phần tử trong list, index in list (cách 2)
# id1 = func_num_ixdex_in_list(subject, 'lịch sử')
func_num_ixdex_of_list = lambda into_list, value_inlist: into_list.index(value_inlist)

