A=float(input('輸入身高\(公尺)'))
B=float(input('輸入體重'))
BMI=B//A**2
if BMI<18.5:
    print('體重不足')
elif BMI<24:
    print('正常')
elif BMI<27:
    print('過重')
elif BMI<30:
    print('輕度肥胖')
elif BMI<35:
    print('中度肥胖')
else:
    print('重度肥胖')






