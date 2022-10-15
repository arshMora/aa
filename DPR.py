import random

#1. Создать список, состоящий из заданного числа элементов, равных 0.
'''
c = [0] * int(input())
print(c)


#2. Организовать ввод элементов списка с клавиатуры. Размер списка также должен задаваться пользователем. Введённый список вывести на экран.
limiter = int(input())
arr = [0] * limiter
i = 0
while i<limiter:
    arr[i] = input()
    i+=1
else: 
    print(arr)


#3.	Дан список, состоящий из n элементов. Вывести элементы списка на экран (в столбик, в строку).
limiter = int(input())
arr = [0] * limiter
for i in range(limiter): 
    print(arr[i])
print(arr)    


#4.	Создать двумерный список (матрицу) 3х3 и заполнить его числами от 0 до 8.
matrix = [[i for i in range(3)] for i in range(3)]
count = 3
for i in range(1,3):
   for j in range(3):
      matrix[i][j] = count
      count += 1
print(matrix) '''


#5.	Дан список из n чисел. Вывести элементы списка, которые больше 7.
# limiter = int(input())
# initArr = [0] * limiter
# secArr = []
# for i in range(limiter):
#     initArr[i] = random.randint(0,10)
#     if initArr[i] > 7:
#         secArr.append(initArr[i])
# print(initArr,'\n', secArr, sep='')

#6.	Дан список из n элементов. Вывести те элементы, у которых чётный (нечётный) индекс
# limiter = int(input())
# initList = [0] * limiter
# evenList = []   #четные
# oddList  = []   #нечетные
# for i in range(limiter):
#     initList[i] = random.randint(0,9)
#     if i%2==0 or i==0:
#         evenList.append(initList[i])
#     else:
#         oddList.append(initList[i])
# print(f"Первоначальный список:\t{initList}")
# print("Четный индекс:\t\t",evenList,'\n',"Нечетный индекс:\t",oddList,sep='')


#7.	Дан список из n элементов. Вывести элементы списка по три в строке.
# limiter = int(input())
# initList = [0] * limiter
# comp = 0
# for i in range(len(initList)):
#     print(initList[i],end='')
#     comp+=1
#     if comp==3:
#         comp=0
#         print('\n',end='')


#8.	Дан список из n чисел. Вывести сумму всех элементов списка
# limiter = int(input())
# initList = [0] * limiter
# sum = 0
# for i in range(limiter):
#     initList[i] = random.randint(0,9)
#     sum+=initList[i]
# print(initList)
# print(sum)


#9.	Дан список из n чисел. Вывести сумму всех чётных элементов списка
# limiter = int(input())
# initList = [0] * limiter
# sum = 0
# for i in range(limiter):
#     initList[i] = random.randint(0,9)
#     if i%2==0 or i==0:
#         sum+=initList[i]
# print(initList)
# print(sum)


#10. Дан список из n чисел. Вывести сумму элементов списка, которые делятся на 4
# limiter = int(input())
# initList = [0] * limiter
# sum=0
# for i in range(limiter):
#     initList[i] = random.randint(0,9)
#     sum+=initList[i] # Все числа делятся на 4 :)
# print(initList)
# print(sum)


#11. Дан список из n чисел. Вывести произведение всех ненулевых элементов списка
# limiter = int(input())
# initList = [0] * limiter
# composition=1
# for i in range(limiter):
#     initList[i] = random.randint(-9,9)
#     if initList[i]!=0:
#         composition*=initList[i]
# print(initList)
# print(composition)


# 12.	Дан список из n чисел. Вывести наибольший элемент в списке.
# 13.	Дан список из n чисел. Вывести наименьший элемент в списке.
# 14.	Дан список из n чисел. Вывести номер наибольшего элемента в списке.
# 15.	Дан список из n чисел. Вывести квадрат наибольшего элемента в списке.
# limiter = int(input())
# initList = [0] * limiter
# maxEl=0
# minEl=0
# maxElNumb = 0
# maxElSquare = 0
# for i in range(limiter):
#     initList[i] = random.randint(-9,9)
#     if maxEl<=initList[i]:
#         maxEl=initList[i]
#         maxElNumb = i
#         maxElSquare = maxEl*maxEl
#     if minEl>initList[i]:
#         minEl=initList[i]
# print(initList)
# print(f"Наибольший элемент в списке: {maxEl}\nНаименьший элемент в списке: {minEl}\nНомер наибольшего элемента в списке: {maxElNumb}\nКвадрат наибольшего элемента в списке: {maxElSquare}")
