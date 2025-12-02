#2.1 TOÁN TỬ SỐ HỌC 

# + Phép cộng
# - Phép trừ
# * Phép nhân
# / Phép chia (kqua là float )
# % Phép chia lấy dư
# ** Phép lũy thừa
# // Phép chia lấy phần nguyên

a = 10
b = 2
print("a + b =", a + b)        # Phép cộng
print("a - b =", a - b)        # Phép trừ 
print("a * b =", a * b)        # Phép nhân
print("a / b =", a / b)        # Phép chia
print("a % b =", a % b)        # Phép chia lấy dư 10 chia 2 dư 0
print("a ** b =", a ** b)      # Phép lũy thừa 10 mũ 2 = 100
print("a // b =", a // b)      # Phép chia lấy phần nguyên 10 chia 2 dc 5 
#lưu ý: Toán tử chia (/) luôn trả về kết quả dưới dạng số thực (float), ngay cả khi phép chia cho ra số nguyên.
# toán tử số học

# == Bằng nhau (a  == b)
# != Khác nhau (a != b)
# > Lớn hơn (a > b)
# < Nhỏ hơn (a < b)
# >= Lớn hơn hoặc bằng (a >= b)
# <= Nhỏ hơn hoặc bằng (a <= b)

a = 10
b = 2
print("a == b:", a == b)      # Bằng nhau 10 ko = 2
print("a != b:", a != b)      # Khác nhau 10 khác 2
print("a > b:", a > b)        # Lớn hơn
print("a < b:", a < b)        # Nhỏ hơn
print("a >= b:", a >= b)      # Lớn hơn hoặc bằng
print("a <= b:", a <= b)      # Nhỏ hơn hoặc bằng
#toán tử so sánh

# = gán ( a = 10)
# += Cộng và gán ( a += 5  tương đương a = a + 5)
# -= Trừ và gán ( a -= 5  tương đương a = a - 5)
# *= Nhân và gán ( a *= 5  tương đương a = a * 5)
# /= Chia và gán ( a /= 5  tương đương a = a / 5)
# %= Chia lấy dư và gán ( a %= 5  tương đương a = a % 5)
# **= Lũy thừa và gán ( a **= 5  tương đương a = a ** 5)
# //= Chia lấy phần nguyên và gán ( a //= 5  tương đương a = a // 5)

a = 10
a += 5
print("a += 5:", a)      # a = 10 + 5 = 15
a -= 3
print("a -= 3:", a)      # a = 15 - 3 = 12
a *= 2 
print("a *= 2:", a)      # a = 12 * 2 = 24
a /= 4
print("a /= 4:", a)      # a = 24 / 4 = 6.0
a %= 4
print("a %= 4:", a)      # a = 6.0 % 4 = 2.0
a **= 3
print("a **= 3:", a)      # a = 2.0 ** 3 = 8.0
a //= 3
print("a //= 3:", a)      # a = 8.0 // 3 = 2.0 
# kqua dùng tiếp mỗi phép tính
# toán tử gán

# and (và) (a and b)
# or (hoặc) (a or b)
# not (phủ định) (not a)

a = True
b = False
print("a and b:", a and b)    # và  True và False = False
print("a or b:", a or b)      # hoặc True hoặc False = True 
print("not a:", not a)        # phủ định  không True = False
# and , or có tính short cỉcuit , nếu dkien đầu tiên đã xác định đc kqua thì k cần xét dkien sau
# toán tử logic

# in (thuộc về, có trong) (a in b)
# not in (không thuộc về, không có trong) (a not in b)

a = 5
b = [1, 2, 3, 4, 5]
print("a in b:", a in b)        # thuộc về 5 có trong danh sách b = True
print("a not in b:", a not in b)  # ( bảo là không có 5 trong b mà b có 5 => false)
# toán tử thành viên

# is (là cùng 1 đtuong) (a is b)
# is not (không phải cùng 1 đtuong) (a is not b)

a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]
print("a is b:", a is b)          # cùng là 10 = True
print("c is d:", c is d)          #  khác vùng nhớ ( 2,1)
print("c is not d:", c is not d)  # vì khác nhau vùng nhớ nên  = True
# toán tử nhận dạng

# thứ tử ưu tiên (chắc còn lâu ms nhớ nổi)
#1. Toán tử trong ngoặc ()
#2. Toán tử lũy thừa **
#3. Toán tử +x , -x và ~x
#4. Toán tử nhân *, chia /, chia lấy phần nguyên //, chia lấy dư %
#5. Toán tử cộng + và trừ -
#6. Toán tử << và >>
#7. Toán tử & (AND)
#8. Toán tử ^ (XOR)
#9. Toán tử | (OR)
#10. Toán tử so sánh ==, !=, >, <, >=, <=, is, is not, in, not in
#11. Toán tử logic not
#12. Toán tử logic and
#13. Toán tử logic or

a = 10
b = 5
c = 2
result = a + b * c  # Phép nhân trước phép cộng
print("Kết quả a + b * c =", result)  # Kết quả: 20
result = (a + b) * c  # Phép cộng trong ngoặc trước
print("Kết quả (a + b) * c =", result)  # Kết quả: 30
# toán tử ưu tiên