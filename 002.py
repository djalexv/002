# 2.1 Ошибки и исключения 6 из 9 шагов пройдено


# ResDict = {}
# for i in range(int(input())):
#     inStr = list(filter(lambda s: s != ':', input().split()))
#     CurKey = inStr[0]
#     CurSet = set(inStr[1:])
#     # print('inStr=', inStr, 'CurKey=', CurKey, 'CurSet=',CurSet)
#     # ResDict[CurKey] = set({CurKey})
#     # print('****', ResDict[CurKey])
#     for j in CurSet:
#         if j in ResDict:
#             # print('j=', j, 'ResDict[j]=', ResDict[j]) #.items())
#             CurSet = CurSet.union(ResDict[j])
#             # print('CurSet=', CurSet)
#     if CurKey in ResDict:
#         ResDict[CurKey] = ResDict[CurKey].union(CurSet)
#     else:
#         ResDict[CurKey] = CurSet
# print('1-', *ResDict.items(), sep='\n', end='\n')
# for k, v in ResDict.items():
#     for elset in v:
#         if elset in ResDict:
#             # print('j=', j, 'ResDict[j]=', ResDict[j])  # .items())
#             ResDict[k] = ResDict[k].union(ResDict[elset])
#             # print('CurSet=', CurSet)
#
# print('2-', *ResDict.items(), sep='\n', end='\n')
# print()
# print()
# inCh = []
# for i in range(int(input())):
#     inStr = input().strip()
#     # pAdd = True # uuuu = len(inCh)
#     if inStr in ResDict:
#         for p in range(len(inCh)):
#             if inCh[p] != inStr:
#                 if inCh[p] in ResDict[inStr]:
#                     print(inStr)
#                     break
#                 # else:
#                 #     pAdd = False
#         # if pAdd:
#         inCh.append(inStr)
# print(inCh)


# parents = {}
# for _ in range(int(input())):
#     a = input().split()
#     parents[a[0]] = [] if len(a) == 1 else a[2:]
#
# print('2-', *parents.items(), sep='\n', end='\n')
#
#
# def is_parent(child, parent):
#     return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))
#
#
# inCh = []
# for _ in range(int(input())):
#     inStr = input().strip()
#     if inStr in parents:
#         for p in range(len(inCh)):
#             # if inCh[p] != inStr:
#             if is_parent(inStr, inCh[p]):
#                 print(inStr)
#                 break
#         inCh.append(inStr)
# print(inCh)
#
# inCh = []
# for i in range(int(input())):
#     inStr = input().strip()
#     # pAdd = True # uuuu = len(inCh)
#     if inStr in ResDict:
#         for p in range(len(inCh)):
#             if inCh[p] != inStr:
#                 if inCh[p] in ResDict[inStr]:
#                     print(inStr)
#                     break
#                 # else:
#                 #     pAdd = False
#         # if pAdd:
#         inCh.append(inStr)

# class NonPositiveError(Exception):
#     pass
#
# class PositiveList(list):
#     def append(self, x):
#         if x > 0:
#             list.append(self, x)
#         else:
#             raise NonPositiveError
#
#
# a = PositiveList()
# a.append(1)

# import sys
#
# for path in sys.path:
#     print(path)

# from datetime import *  # timedelta, date, time

# import datetime
# from time import strptime

# inStr = [int(_) for _ in input().split()]
# inDate = date(inStr[0], inStr[1], inStr[2])
# print(inDate)
# sDate = datetime.strptime(input().strip(), "%Y %m %d") + timedelta(days=int(input().strip())) !!!!!!!!!!!!_--------------
# print(type(sDate))
# print(sDate.year, sDate.month, sDate.day) # + timedelta(days=int(input().strip()))).
# print(sDate.strftime("%Y %n %e"))
# print(strptime((date(inStr[0], inStr[1], inStr[2])+timedelta(days=int(input().strip()))), "%Y %m %e"))
# print(type(date(strptime(input().strip(), "%Y %m %d"))))
# print(type(date(inStr[0], inStr[1], inStr[2])))

# 2.2 Работа с кодом: модули и импорт 8 из 9 шагов пройдено

# from simplecrypt import decrypt, DecryptionException
#
# outString =[]
# with open("encrypted.bin", "rb") as datafile, open('_passwords.txt') as passwordsFile:
#     encrypted = datafile.read()
#     for InLine in passwordsFile:
#         print(InLine.strip())
#         try:
#             outString.append(decrypt(InLine.strip(), encrypted))
#         except DecryptionException as e:
#             print(e)
#
# print(outString)
#

from random import random

def random_generator(k):
    i: int
    for i in range(k):
        # print(i)
        yield i #random()


g = random_generator(3)
# print(g)
for i in g:
    print(i)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


class multifilter:
    def judge_half(pos, neg):
        return pos >= neg
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return pos >= 1
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        return self
        # возвращает итератор по результирующей последовательности