#Task1
sq = int(input('Площадь участка, соток: ')) #ввод площади участка (10 соток)
a = int(input('Длина грядки, м: ')) # default 15 m
b = int(input('Ширина грядки, м: ')) # default 10 m

sqm = sq * 100 #перевод площади участка в м2
sqg = a * b #площадь грядки, м2
n = sqm // sqg # количество грядок
ost = sqm - n * sqg # остаток площади

print('Незанятая площадь:', ost, 'м2')
