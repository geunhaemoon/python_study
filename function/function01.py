#def(define) - > 함수를 정의한다

# 오버 로딩 안됨 !!!
def add(x,y):
    result = x + y
    return result

# 매개변수, 여러개의 리턴은 튜플 자료형으로 정의된어진다.
def add(*a): # 튜플로 받겠다.....
    print(type(a))
    return list(a), 10

r = list(add(20, 10, 5, 30, 40))

print(r)

# **이면 딕셔너리 자료형이 매개변수를 변환해준다
def sub(**data):
    print(type(data))
    print(data)

sub(a=1, b=2)

def sub(data):
    print(type(data))
    print(data)

sub({"a":1, "b":2})


def connection(ip="127.0.0.1", port="8080", serverName="", username="root", password=""):
    print(f"ip : {ip}")
    print(f"port : {port}")
    print(f"serverName : {serverName}")
    print(f"username : {username}")
    print(f"password : {password}")

connection("127.0.0.1", "8080", "test_server", "root", "1q2w3e4r", port="3306")

a = 2 # 전역함수 

def multi(a):
    return a **2

a= multi(a)
print(a)

def div():
    global a # global 써서는 전역함수 들고올수있고 그냥은 못들고옴
    a = a * 10

    div()
    print(a)

def add(a, b):
    return  a+b

print(add(10, 20))


#파이썬에서 람다는 하나의 명령인 수행을 할 수 있다 (여러줄 불가능)
add = lambda  a,b: a + b

add(30,30)