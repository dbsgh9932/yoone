x=int(input('예금액 입력 : '))
y=float(input('이자율 입력(%) : '))
z=int(x*y/100)
r=x+z
print('-------------')
print('예금액 : %d원'%x)
print('이자율 : %.1f%%'%y)
print('예금이자 : %d원'%z)
print('잔액 : %d원'%r)
print('-------------')
print('예금액 : %s원'%format(int(x),','))
print('이자율 : %.1f%%'%y)
print('예금이자 : %s원'%format(int(z),','))
print('잔액 : %s원'%format(int(r),','))
print('-------------')
