#2.2 VÀO RA TRONG PYTHON\

#print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)
# k nhớ nổi nma cứ ghi ra để cho có :((
print ("D25 Greetings!") # chuỗi
print ("D25", "Greetings", sep="-", end="!\n") # nhiều đối tượng
x = ("Apron","Belt","Cap") # tuple
print (x)

# input (
# prompt )  (1 chuỗi tùy chọn)
name = input("enter your name :")
print ("Hello," + name + "!")
# nhập tên và print ra

number = int(input("Nhập 1 số nguyên: "))
print("Số bạn mới nhập là :", number)
# nhập số nguyên và in ra 

num1 = int(input("Nhập số thứ 1:"))
num2 = int(input("Nhập số thứ 2:"))
sum = num1 + num2
print("Tổng của", num1,"và", num2, "là :", sum)
# nhập 2 số , tính tổng và in kqua

Values = input("Nhập nhiều giá trị, cách nhau bằng khoảng trắng: ").split(",")
print("Giá trị bạn vừa nhập là:", Values)
# nhập nhiều gtri cách bởi dấu cách , split() dùng để tách chuỗi