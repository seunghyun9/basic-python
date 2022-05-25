#while 사용


prompt = '''
    1.Add
    2.Del
    3.List
    4.Quit
    Enter Number: '''
number = 0
while number != 4:
    print(prompt)
    number = int(input());

#coffee
coffee = 10
while True:
    money = int(input("투입할 돈을 입력 해주세요."))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money >300:
        print("커피와 잔돈을 %d원받아가세요" % (money-300))
        coffee = coffee -1
    else: print("커피를 지급하지 않습니다. 남은 커피양은 %d개입니다." % coffee)
    if coffee ==0:
        print("커피가 다 떨어졌습니다.")
        break

# continue
z=0
while z<10 :
    z = z +1
    if z %2 ==0 :continue
    print(z)