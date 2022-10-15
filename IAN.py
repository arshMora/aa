import queue
from random import *
from collections import deque
from pprint import pprint


'''
1.Используя стек, напечатать символы некоторой величины строкового типа в обратном порядке.
'''
# def stack_reverse():
#     stack_item = deque()
#     stack_item.extend(['a','b',1,2,3,4,5,6,7])
#     print(stack_item)
#     stack_item_length = len(stack_item)
#     new_stack_item = deque()
#     for _ in range(stack_item_length):
#         new_stack_item.append(stack_item.pop())
#     print(new_stack_item)

# stack_reverse()

'''
2.Дана величина a строкового типа из четного количества символов. 
Получить и напечатать величину b, состоящую из символов первой половины
величины a, записанных в обратном порядке, после которых идут символы второй половины величины a,
также записанные в обратном порядке. Например, при а = “привет” b должно быть равно “ипртев”.
'''
# def secondTask(a):
#     #проверка четности
#     if len(a)%2==0:
#         b = deque()
#         bFirst= deque()
#         bSecond= deque()
#         # половинчатя длина величины a
#         aSliceLength = int(len(a)/2) 
        
#         #делю величину a на две части и записываю в соответствующие переменные bFirst и bSecond
#         while len(bSecond)<aSliceLength:
#             bSecond.append(a.pop())
#         # print(bSecond)
#         while len(bFirst)<aSliceLength:
#             bFirst.append(a.pop()) 
#         # print(bFirst)
#         # Соединяю части в один стек
#         b = bFirst + bSecond
#         return b
#     else:
#         return 'Not even-number'

# a = deque()
# a.extend(str(input()))
# print(secondTask(a))

'''
3.Составить программу, в которой все делители (в том числе и симметричные) заданного 
числа n будут выводиться в порядке возрастания (при проверке возможных делителей, не превышающих √n).
'''
# def thirdTask():
#     s=deque()
#     s.append(1)
#     n=int(input('Введите число: '))
#     if n == 1:
#         return s
#     i = 2
#     while i < n:
#         if n%i==0:
#             s.append(i)
#         i+=1
#     s.append(n)
#     return s

# print(thirdTask())

'''
4.Дан входной файл: stack.in Получить выходной файл: stack.out
Во входном файле, в каждой строке содержится операция со стеком 
Операция — это либо “+ N”, либо “-”. Операция “+ N” означает добавление в стек числа N. 
Команда “-” означает изъятие элемента из стека. Гарантируется, что не происходит извлечения из пустого стека.
Необходимо для каждой операции изъятия элемента из стека выводить результат изъятия в выходной файл. 

Формат входного файла: в первой строке входного файла содержится количество операций — M.
Каждая последующая строка исходного файла содержит ровно одну операцию. 
Формат выходного файла: числа, которые извлекаются из стека, расположены по одному в каждой строке. 
Пример входного и выходного файлов:
stack.in	stack.out
6	        7
+3          23
+7	
-	
+51	
+23	
-	
'''
# def fourthTask():
#     stackIn = deque()
#     stackOut = deque()
#     # рандом плюса и минуса
#     utilPM = ('-','+')
#     #pM = choice(utilPM)
#     # определяем количество операций (первая строка)
#     countPlusMinus = randint(5,10)
#     # заполняем первый стек
#     # сперва количество операций
#     stackIn.append(countPlusMinus)
#     # определяем второй элемент всегда с операцей плюс
#     firstEl=str(randint(0,99))
#     stackIn.append('+'+firstEl)
    
#     # запоминаем знак и число предыщего элемента стека
#     prevPM = '+'
#     prevEl = firstEl
#     # заполняем стек операциями с числами
#     while len(stackIn)<countPlusMinus:
#         # выбор плюса или минуса
#         pM = choice(utilPM)
#         if pM == '+':
    #         prevEl = str(randint(0,99))
    #         stackIn.append(pM + prevEl)
    #     else:
    #         # при последующем минусе
    #         if prevPM == '-':
    #             prevPM = utilPM[1]
    #             pM = utilPM[1]
    #             prevEl = str(randint(0,99))
    #             stackIn.append(pM + prevEl)
    #         else: 
    #             stackIn.append(pM)
    #             stackOut.append(prevEl)
    #             prevPM = pM
    # [print(i, end="\n") for i in stackIn],print('\n')
    # [print(i, end="\n") for i in stackOut]
    
# fourthTask()

'''
5.Реализовать работу очереди. Для каждой операции изъятия элемента вывести её результат. 
На вход программе подаются строки, содержащие команды. 
Каждая строка содержит одну команду. Команда — это либо “+ N”, либо “-”. 
Команда “+ N” означает добавление в очередь числа N. Команда “-” означает изъятие элемента из очереди. 
Формат входного файла: в первой строке содержится количество команд — M, 
в последующих строках содержатся команды, по одной в каждой строке. 
Формат выходного файла: числа, которые удаляются из очереди??????????????, 
расположены по одному в каждой строке. 
Пример входного и выходного файлов:
queue.in	queue.out
5	        12
+12	        8??
+8	
-	
+234	
-
'''
# def fifthTask():
#     queueIn = deque()
#     queueOut = deque()
#     # рандом плюса и минуса
#     utilPM = ('-','+')
#     # определяем количество операций (первая строка)
#     countPlusMinus = randint(5,10)
#     # заполняем первый стек
#     # сперва количество операций
#     queueIn.append(countPlusMinus)
#     # определяем второй элемент всегда с операцей плюс
#     # запоминаем знак и число предыщего элемента стека
#     prevPM = '+'
#     prevEl=str(randint(0,99))
#     queueIn.append('+'+prevEl)
    
#     #начинаем с 3 строки
#     while len(queueIn)<countPlusMinus:
#         # выбор плюса или минуса
#         pM = choice(utilPM)
#         # при последующем плюсе
#         if pM == '+':
#             queueOut.append(prevEl)
#             prevEl = str(randint(0,99))
#             queueIn.append(pM + prevEl)
#         else:
#             # при последующем минусе
#             if prevPM == '-':
#                 prevPM = utilPM[1]
#                 pM = utilPM[1]
#                 prevEl = str(randint(0,99))
#                 queueIn.append(pM + prevEl)
#             else: 
#                 queueIn.append(pM)
#                 # queueOut.pop()
#                 prevPM = pM
#     [print(i, end="\n") for i in queueIn],print('\n')
#     [print(i, end="\n") for i in queueOut]
    
# fifthTask()
















# people = ["Sam","Tom", "Sam", "Bob", "Sam",]
# people.insert(4,people.pop(3))
# print(people)

# добавляем пустой элемент для проверки пустого элемента стека,
#     # т.к. из пустого стека извлечение не может происходить
#     queueIn.append(0)
#     if bool(queueIn[1]):
#         None
#     # определяем второй элемент всегда с операцей плюс
#     else:
#         queueIn.pop()
#         firstEl=str(randint(0,99))
#         queueIn.append('+'+firstEl)