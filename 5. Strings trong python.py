#5. STRING TRONG PYTHON

# string dùng ngoặc đơn '
# Tạo string bằng dấu đơn '
string1 = 'Hello, Python!'
print(string1)
# Tạo string bằng dấu kép "
string2 = "Hello, Python!"
print(string2)
# string nhiều dòng là 3 dấu đơn ''' 
string3 = '''This is a
multiline string.'''
print(string3)
# string nhiều dòng là 3 dấu kép """ 
string4 = """This is also a
multiline string."""
print(string4)

#truy câp = chỉ số index
string = "Hi,Duo!"
print(string[0])
print(string[1])
print(string[-1])
print(string[-2])
#truy cập gtri

#string k thể bị thay đổi ndung nhưng có thể tạo string mới = vc kết hợp các ptu string cũ vs gtri mới
string = "Duo, hi!"
new_string = string[:4] + 'halo!'
print (new_string)
#lấy Duo, và + thêm halo!
#cập nhập string'

# \n : xuống 
# \t: Tab
# \\: Dấu gạch chéo ngược
# \': Dấu nháy đơn
# \": Dấu nháy kép

string = "Hello,\nPython!\tWelcome to the world of \\strings\\."
print(string)
# ký tự thoát

# + : kết hợp 2 strings
# - : lặp 1 string nhiều lần
string1 = "Helloo"
string2 = "Duong"
combined_string = string1 + string2
print (combined_string)
repeated_string = string1 * 3
print (repeated_string)
# toán tử dbiet vs strings

# pphap format và f strings
name = "Python"
age = 30
formatted_string = "Hello, %s! You are %d years old." % (name, age)
print(formatted_string) #dùng %
formatted_string = "Hello, {}! You are {} years old.".format(name, age)
print(formatted_string) #dùng format
formatted_string = f"Hello, {name}! You are {age} years old."
print(formatted_string) #dùng f-strings
# toán tử dạng chuỗi

student1 = "nguyen van a"
print(name.title())
student2 = "NGUYEN VAN B"
print(student2.title())
student3 = "Nguyen Van C"
print(student3.title())
#dùng title

text = "This is a string."
upper_text = text.upper()
print("Upper case:", upper_text) #in hoa hết
lower_text = text.lower()
print("Lower case:", lower_text) # thg hết
#upper và lower

first_name = "Nguyen"
last_name = "Van"
full_name = first_name + " " + last_name
print(full_name)
message = "Hello, " + full_name.title() + "!"
print(message)
#Kết hợp hoặc nối chuỗi
#rstrip() - xóa khoảng trắng bên phải của chuỗi
#lstrip() - xóa khoảng trắng bên trái của chuỗi
#strip() - xóa khoảng trắng ở cả hai bên của chuỗi

text = "    This is a string.    "
second_text = "!"
rstrip_text = text.rstrip()
lstrip_text = text.lstrip()
strip_text = text.strip()
print("Rstrip:", rstrip_text + second_text)
print("Lstrip:", lstrip_text + second_text)
print("Strip:", strip_text + second_text)
# xóa khoảng trắng

text = "this is a text."
print(text.capitalize()) #kí tự đầu tiên in hoa
#capitalize

text = "center"
x = text.center(20, '*')
print(x, len(x)) # cho ra giữa , xung quanh dấu *
#center(length, char)

text = "This is a string. This is another string. This is a third string."
print("Number of 'string' in text:", text.count("string"))
print("Number of 'This' in text:", text.count("This"))
print("Number of 'string' in text from position 10 to position 20:", text.count("string", 10, 20))
#count(value) dùng text,count để dếm chữ lặp

text = "This is a string."
print(text.endswith("string."))
print(text.endswith("is")) #kết thúc = chữ cuối thì true , k thì false
#endswth

text = "This is a string"
print("Index of 'is' in text:", text.find("is"))
#find để tìm vtri đầu , rfind là cuối , k tìm thấy thì -1
#find và rfind

text1 = "This Is A String."
text2 = "4564654654654654"
text3 = "this is an alphanumeric string 4564654654"
text4 = "-45646546"
print(text1.isalnum()) #chứa số và chữ cái
print(text1.istitle()) #
print(text1.isalpha()) # chứa chữ cái alphabet
print(text2.isnumeric())
print(text3.islower()) # viết thg
print(text4.isnumeric())
#idk this tbh

myList = ["as", "ba", "cd"]
x = "-".join(myList)
print(x) #as-ba-cd
#join

text = "This is a string. This is another string. This is a third string."
print(text.replace("string", "text"))
print(text.replace("This", "That"))
#thay string = text , thay this = that
#replace

text = "This is a string. This is another string. This is a third string."
numbers = "1,2,3,5,6,7"
string_list = text.split(" ")
number_list = numbers.split(",")
print(string_list)
print(number_list)
#tách số và chữ
#split

#B1
s = input("Nhập chuỗi: ")
print("In hoa chữ cái đầu tiên:", s.capitalize())
print("In hoa chữ cái đầu mỗi từ:", s.title())
print("In hoa toàn bộ:", s.upper())
print("In thường toàn bộ:", s.lower())
#B2
name = "Albert Einstein: "
quote = "A person who never made a mistake never tried anything new."
name_quote = name + quote
print(name_quote)
#B3
s = input("Nhập chuỗi: ")
print("Chỉ chứa số (0-9):", s.isdigit())
print("Chỉ chứa kí tự alphabet:", s.isalpha())
print("Chỉ chứa số và kí tự alphabet:", s.isalnum())
print("Tất cả kí tự đều viết hoa:", s.isupper())
print("Tất cả kí tự đều viết thường:", s.islower())
#B4
s = input("Nhập vào một chuỗi gồm nhiều từ: ")
print("Chuỗi bạn vừa nhập là:", s)
