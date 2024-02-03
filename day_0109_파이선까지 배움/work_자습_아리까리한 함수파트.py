# 아리까리한 함수파트 공부해봄 !

# unit30 함수에서 위치 인수와 키워드 인수 사용하기

def print_numbers(*x):
    print(x)

def print_numbers2(y):
    print(y)

A = [1, 2, 3]

print('1')
print_numbers(A)
print_numbers(*A)
print()

print('2')
print_numbers2(A)
#print_number2(*A)       #언패킹해서 들어갔지만 함수는 하나의 변수만 들어가니까 에러..


def info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

info('임소영', 18, '중구')
print()


def information(**data):
    print(data)
    print(type(data))
    for k,v in data.items():
        print(k)
        print(type(k))
        print(v)
        print(type(v))


myDict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
information(**myDict)

