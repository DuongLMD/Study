#3. CẤU TRÚC LỆNH RẼ NHÁNH

#if condition:
# condition là boolean nên sẽ trả true hoặc false
# true thì thực hiện lệnh trong khối lệnh if
# false thì bỏ qua khối lệnh if và tiếp tục thực hiện các lệnh bên ngoài khối lệnh if

age = 18
if age >= 18:
    print("Bạn đủ tuổi để bỏ phiếu.")
#18 thì print
#if

#if condition: true thì dùng , ko thì chuyển sang else
#else: if sai  nên dùng else

age = 16
if age>= 18:
    print ("Bạn đủ tuổi")
else:
    print ("bạn chưa đủ tuổi")
# 16t thì false , 18 hoặc trên thì ttrue
#if else

# if condition1:
#elif condition2: 1 sai 2 đúng
#elif condition3: 2 sai 3 đúng
#else: tất cả sai

score = 50
if score >= 90:
    print ("Xuất sắc")
elif score >= 75:
    print ("Giỏi")
elif score >= 60:
    print ("Khá")
else:
    print ("Trung bình hoặc dưới trung bình")
#đúng thì dừng k thì chạy đến khi đúng hoặc sai hết
#if , elif , else

age = 20
citizen = "vn"
if age >= 18:
    if citizen == "vn":
        print ("đủ đk đki")
    else:
        print ("khong phải vn")
else:
    print ("chưa đủ tuổi")
#lệnh rẽ nhánh lồng nhau ( nested if )

#and : tất cả đúng
#or : ít nhất 1 đúng
#not : phủ định

age = 20
citizen = "vn"
if age >= 18 and citizen == "vn":
    print ("đủ dk")
else:
    print ("ko đủ dk")
#toán tử logic kết hợp

# ss số , chuỗi , vv

x = 10
y = 20
if x < y:
    print ("x nhỏ hơn y")
elif X > y:
    print ("x lớn hơn y")
else:
    print ("x bằng y")
#ss số
name = "Duo"
if name == "Duo":
    print ("Hi , Duo!")
else:
    print ("intruder alert")