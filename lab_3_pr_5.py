a=int(input('введите первое число:_'))
b=int(input('введите второе число:_'))
if b==0:
    print('на ноль делить нельзя')
elif a%b!=0:
    print(a//b)
    print('остаток ',a%b)
else:
    print('частное', a//b)
    print('делится без остатка')

    