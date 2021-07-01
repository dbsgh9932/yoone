# 디폴트 매개변수(파라미터)
# 매개변수에 기본값 지정 - 호출 할 때 인수가 넘어오면 넘어오는 인수 사용 / 인수가 안넘어오면 기본값 사용

def greet(name,msg='안녕 ^^'): # name 매개변수 : 반드시 인수가 필요
                              # msg 매개변수 : 인수가 전달되면 사용, 안넘어오면 기본값 사용
    print(name+','+msg)

greet('홍길동','잘 지내죠?')
greet('김철수')
###### 디폴트 매개변수는 맨 마지막에 위치!!!!
