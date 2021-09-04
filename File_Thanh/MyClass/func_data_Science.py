 

"1.Danh mục tổng hợp các hàm xử lý"
#Lọc chuỗi giữa 2 ký tự:
def func_get_Str_between_two_specical( chr1, in_str, chr2):
    "Tìm chuỗi nằm trong 2 ký tự đặc biệt"
    str_out =[]
    for i, s in enumerate(in_str):
        if s == chr1:
            begin = i
        elif s == chr2:
            after = i+1
            str_out.append(in_str[begin+1:after-1])
    return str_out

# Đọc lọc chuỗi list nằm giữa 2 ký tự đặc biệt
def filter_list_betwen_2_char_special(chr1, in_list, chr2):
    list_Datas = []
    for data in in_list:
        row_data = func_get_Str_between_two_specical(chr1, data,chr2)    
        if row_data != []:
            list_Datas.append(row_data)
    return list_Datas

# Lọc dữ liệu trùng trong 1 list
def remove_duplicate_data(list_Datas):
    duplicate_data =[]
    for data in list_Datas:
        if data not in duplicate_data:
            duplicate_data.append(data)
    return duplicate_data
    # print(len(datas), len(list_Datas))

# Tìm mã chứng khoán
def fun_find_code(in_Str, in_list):
    in_Str = in_Str.replace("'","")
    in_Str = in_Str.strip()

    for code in in_list:        
        if str(code[0]) == str(in_Str):
            return  str(code[1])
            

# remove các dấu "'", khoảng cách space trong list_Datas
def fun_clean_list_Datas(list_Datas):
    list_out = []
    for row in list_Datas:
        row[0].replace("'","")
        row[0] = row[0].strip()
        list_out.append(row[0])        
    return list_out

#Lọc chuỗi giữa 2 ký tự:
def func_get_Str_year( chr1, in_str, chr2):
    "Tìm chuỗi nằm trong 2 ký tự đặc biệt"
    str_out =[]
    begin = 0
    after = 0
    nam = ""
    for i, s in enumerate(in_str):
        if s == chr1:
            begin = i+1
        elif s == chr2:
            if begin !=0:
                after = i
                str_out.append(in_str[begin:after])
                begin = 0
    for s in str_out:
        len_s = len(s)
        if len_s>=4:
            if len(s)== 4 and s.isdigit():
                nam = s
                break         
            else:
                for i in range(len(s)):
                    if (i+5) <= len_s and (s[i:i+5].isdigit())>2000:
                        nam = s[i:i+5]
                        break
    return nam

# Xử lý quarters. Tìm quý nào?
def fun_quarters(str):
    """'CBTT:Tin Định kỳ\n    Năm tài chính\n*\n2021\nQuý\n*\n2
\nNgày ký ban hành\n*\nTrích yếu\n*\nBáo cáo tài chính Quý 2 2021 Hợp nhất PVcomBank\nToàn văn báo cáo tài chính\n*\n2021.02.Q2_HN.pdf\nTải_xuống'"""
    str = str.lower()
    str_quy = str    

    quy = ''
    năm = ''
    audit = 0
    quy_1 =['q1','q1/','q1.', 'q1 -','q1-', 'quý 1', 'quý1']
    quy_2 =['q2','q2/','q2.', 'q2 -','q2-', 'quý 2', 'quý2']
    quy_3 =['q3','q3/','q3.', 'q3 -','q3-', 'quý 3', 'quý3']
    quy_4 =['q4','q4/','q4.', 'q4 -','q4-', 'quý 4', 'quý4']

    # Tìm bán niên, 6 tháng gán cho quý
    if ("6 tháng" or "6t" or "bán niên") in str_quy:
        quy = "bán niên"
        audit = "1"

    elif quy == '':
        str_quy = str_quy.replace('quý\\n*\\n',"quý")
        for q in quy_1:
            if q in str_quy:
                quy = "1"
                break
        if quy == '':
            for q in quy_2:
                if q in str_quy:
                    quy = "2"
                    break
            if quy == '':
                for q in quy_3:
                    if q in str_quy:
                        quy = "3"
                        break
                if quy == '':
                    for q in quy_4:
                        if q in str_quy:
                            quy = "4"
                            break
        
    str_nam = str_quy.replace("\\n*\\n","{")
    str_nam = str_nam.replace("\\n","}")
    nam = func_get_Str_year( "{", str_nam, "}")
    if quy =="":
        audit = "1"

    return quy, nam, audit
    

def export_list(list_Datas, table_seach_tickers):    
    # header = ['No','Ticker', 'Company', 'Quarter', 'Year', 'Audit', 'Resources', 'Date_sended']
    out_list = []
    # out_list.append(header)

    for data in list_Datas:        
        row = data.split(',')
        # da = data[0].split(",")
        no = row[0]
        no = no.replace("'","")

        ticker = row[6] 
        ticker = ticker.replace("'","")       

        # tìm mã chứng khoán từ table_seach_tickers       
        resources = fun_find_code(ticker, table_seach_tickers) #     
        # resources = resources.replace("'","")  
        
        company = row[3]
        company = company.replace("'","") 

        # Tìm quarter
        quarters = row[7]+ row[8]
        quarter, year, audit = fun_quarters(quarters)

        date_sended = row[4]
        date_sended = date_sended.replace("'","")

        out_list.append([no,ticker, company, quarter, year, audit, resources, date_sended])

    return out_list