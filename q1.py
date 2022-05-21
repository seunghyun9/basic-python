# 기본 format 함수
a = "I eat {0} apples".format(3)
print(a)
b = "I eat {0} apples".format("five")
print(b)
n1 = 10
day1 = "three"
c = "I eat {0} apples. so I sick for {1} days".format(3, "five")
d = "I eat {0} apples. so I sick for {1} days".format(n1, day1)
e = "I ate {xo} apples. so i sick for {uo} days".format(xo=18, uo=3)
print(c)
print(d)
print(e)

f = "{0:!<10}".format("hi")
print(f)

# 문자열 포매팅
name = "강영식"
age = 31
h = f'내이름은 {name}이고 나이는 내년에 {age}이다.'
print(h)

# 포매팅 딕셔너리 활용
a1 = {'name':'강영식','age': 32}
a2  = f'내이름은 {a1["name"]}이고 나이는 2년 후에 {a1["age"]}이다.'
print(a2)