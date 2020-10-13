from lec_3_my_module import a #Инструкция, копирующая определённые атрибуты модуля
print(a)

from lec_3_my_module import a,b,c #можно так
print(a*b+c)

from lec_3_my_module import * #Инструкция, копирующая все атрибуты модуля
print(a*d)