#Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше
# издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность
# выручки (соотношение прибыли к выручке). Далее запросите численность
# сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Введите сумму выручки за прошедьший период: "))
expens = int(input("Введите сумму издержек за прошедьший период: "))
if proceeds < expens:
    print('Данный период был убыточным. \nУбытки составили :', expens - proceeds)
elif proceeds > expens:
    profit = proceeds - expens
    print('Данный период был прибыльным. \nПрибыль составила :', profit)
    personal = int(input('Введите кол-во сотрудников: '))
    profit_peson = round(profit / personal, 2)
    print('Прибыль на одного сотрудника составила: ', profit_peson)
