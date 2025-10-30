from math import sqrt 
'''Nhập vào 3 cạnh của tam giác, kiểm tra tính hợp lệ của tam giác, Sau đó tính diện tích 
theo công thức Herong:
Diện tích = sqrt(p*(p-a)*(p-b)*(p-c)) với p = cv/2, cv = a+b+c
'''
print("Chương trình tính diện tích Tam Giác") 
a=float(input("Nhập cạnh a>0:")) 
b=float(input("Nhập cạnh b>0:")) 
c=float(input("Nhập cạnh c>0:")) 
if (a<=0 or b <=0 or c <=0) or (a+b)<=c or (a+c)<=b or b+c<=a: 
    print("Tam giác không hợp lệ") 
else: 
    cv=a+b+c 
    p=cv/2 
    dt=sqrt(p*(p-a)*(p-b)*(p-c)) 
    print("Diện tích =",dt)
    