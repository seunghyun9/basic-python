# 딕셔너리 = 사전, 그대로 이해

# 딕셔너리 생성
dic1 = {'name': '홍길동', 'phone' : '010-2234342'}
print(dic1['name'])

# 딕셔너리 추가
dic1['city'] ='seoul'
print(dic1)

# 딕셔너리 삭제
del dic1['phone']
print(dic1)

#Q6
a = [ 1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

#Q1
a1 = 80 + 75 +77
b1 = a1 / 3
print(b1)

a2 = 13
a2 // 2
a2 % 2

pin = "881120-1068324"
yyyymmdd = "19"+ pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
print(pin[7])

# Q5
a3 = "a:b:c:d"
b3 = a3.replace(":","#")
print(b3)

# Q7
a4 = ['Life','is','too','short']
b4 = " ".join(a4) #공백 사이에 a4 join
print(b4)

#Q8
a5 = (1,2,3)
b5 = a5 +(4,)
print(b5)

#Q10
a6 = {'x':90,'y':80,'z':70}
b6 = a6.pop('y')
print(a6)
print(b6)

#Q11
a7=[1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a7)
b7 = list(aSet)
print(b7)

# Q12
a8 = b8 = [1, 2, 3]
b8[1] = 4
print(a8)

# 합집합 set1 | set2
# 교집합 set1 & set2
# 차집합 set1 - set2

money = True
if money:
    print("택시를")
    print("타고")
    print("가라")