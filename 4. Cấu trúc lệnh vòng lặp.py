#4. CẤU TRÚC LỆNH VÒNG 

#for variable in iterable:
#iterable có thể là dsach (list, tuple, string, set, range) hoặc object có thể lặp 
#variable dùng tùng  gtri trong iterable
# hết iterable thì dừng vòng lặp

for i in range(3): # 0 , 1 , 2 là đủ 3 số
    print(i)

for i in range(1,10,2): #từ 1 đến 9 , cách 2 dvi
    print(i)
#B1
for i in range(1,101):
    if i % 2 == 0:
        print(i)
#B2
total = 0
for i in range(1,11):
    total += i
print (total)
#vòng lặp for dùng range()

#while condition:
# là biểu thức bool
# true thì lặp
# false thì dừng và thực hiện lệnh khác

count = 0
while count < 2 :
    print ("count =",count)
    count += 1
#quên tăng hoặc thay đổi count thì có thể thành lặp vô hạn
#vòng lặp while

#break
for i in range(10):
    if i == 5:
        break
    print(i) #đếm từ 1 - 10 , đến 5 thì break nên dc tử 1 - 4
#continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i) #skip số chẵn
#else
#for item in iterable:
    #if điều_kiện:
        #break
#else:
#else dùng nếu vòng lặp kết thúc k dùng break
#trg lặp có break thì bỏ qua else
for n in range(2, 10):
    for d in range(2, n):
        if n % d == 0:
            print(f"{n} = {d} * {n//d}")
            break
    else:

        print(f"{n} là số nguyên tố")







