#2.1 BIẾN TRONG PYTHON
x = 2
y = "Duo"
print (x)
print (y)
#

x = 2
print (id(x))
#địa chỉ bộ nhớ của biến x

x = 2
x = "Duo"
print (x)
#Gán giá trị cho biến mới nhất

x = 2
print(x)
del x
#Xoá biến x khỏi bộ nhớ , gây lỗi khi in x (print ())

x = 2
y = "Duo"
print(type(x)) #số là kiểu int
print(type(y)) #chữ là kiểu str
#Lấy kiểu biến

x = str(1) # sẽ là chuỗi '1'
y = int(1) # sẽ là số nguyên 1
z = float(1) # sẽ là số thực 1.0
print (x)
print (y)
print (z)
#ép kiểu biến ( chỉ định dữ liệu 1 biến)

a = 2
A = "Duo"
print (a)
print (A)
# phân biệt chữ hoa và chữ thường trong tên biến

x, y, z = "Apple", "Blueberry", "Corn"
print (x)
print (y)
print (z)
# gán nhiều biến trong 1 dòng ( cho gọn code....?)
x = y = z = "omg"
print (x)
print (y)
print (z)
# gán 1 giá trị cho nhiều biến ( idk why would u do that but ok )

#Quy tắc đặt tên biến
#Tên biến trong Python phải tuân theo các quy tắc sau:
#Tên biến phải bắt đầu bằng một chữ cái hoặc dấu gạch dưới (_).
#Tên biến không được bắt đầu bằng chữ số.
#Tên biến chỉ có thể chứa các ký tự chữ cái, chữ số và dấu gạch dưới (A-z, 0-9, và _).
#Tên biến phân biệt chữ hoa chữ thường.
user_age = 18 # đúng
website = "example.com" # đúng
#1password = true # sai, bắt đầu bằng chữ số

def sum(x,y):
    sum = x + y
    return sum
print (sum(2,3))
#Đặt tên biến trùng với từ khoá hệ thống ( không nên làm ) ( cái này là vsc suggest not me)
#Biến cục bộ dc dnghia trg 1 làm và chỉ dc truy cập bên trg hàm đó

x = 2
y = 3
def sum():
    return x + y
print (sum())
#Biến toàn cục dc định nghĩa bên ngoài hàm và có thể truy cập từ bất kỳ đâu trong mã.
#là k cần khai báo vì ghi sẵn x vs y là gì r

PI = 3.14  # Hằng số đại diện cho số Pi
GRAVITY = 9.81  # Hằng số đại diện cho gia tốc trọng
# Đặt tên biến cho hằng số ( không nên thay đổi giá trị của nó trong suốt chương trình)
#để in hoa tên biến để biểu thị rằng nó là một hằng số.









