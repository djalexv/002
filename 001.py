# class MoneyBox:
#     def __init__(self, capacity):
#         self.count = 0
#         # assert isinstance(capacity, object)
#         self.capacity = capacity
#
#     def can_add(self, v):
#         if self.count + v <= self.capacity:
#             return True
#         else:
#             return False
#
#     def add(self, v):
#         # out = self.capacity - self.count
#         if self.can_add(v):
#             self.count += v
#             # out = True
#         return self.capacity - self.count

#
# x = MoneyBox(10)
# print(x.count, x.add(10), x.count, x.can_add(10), x.add(10), x.count)


# class Buffer:
#     def __init__(self):
#         self.buf = list()
#
#
#     def add(self, *a):
#         self.buf += a
#         # if len(self.buf) >= 5:
#         while len(self.buf) >= 5:
#             print(sum(self.buf[:5]))
#             self.buf = self.buf[5:]
#
#
#     def get_current_part(self):
#         return self.buf
#
#
#
# k = Buffer()
# k.add(1, 2, 2, 3)
# print(k.get_current_part())
# k.add(5, 6, 7, 8, 4, 5, 4, 4, 8, 8, 8, 9, 9, 9, 5, 5, 4, 8)
# print(k.get_current_part())


# class A:
#     val = 1
#
#     def foo(self):
#         A.val += 2
#
#     def bar(self):
#         self.val += 1
#
#
# a = A()
# b = A()
#
# a.bar()
# a.foo()
#
# c = A()
#
# print(a.val)
# print(b.val)
# print(c.val)
#
# print(a.__dict__)
# print(b.__dict__)
# print(c.__dict__)

# def Chek

# 1.6 Наследование классов 9 из 9 шагов пройдено

# ResDict = {}
# for i in range(int(input())):
#     inStr = list(filter(lambda s: s != ':', input().split()))
#     CurKey = inStr[0]
#     CurSet = set(inStr[1:])
#     # print('inStr=', inStr, 'CurKey=', CurKey, 'CurSet=',CurSet)
#     ResDict[CurKey] = set({CurKey})
#     # print('****', ResDict[CurKey])
#     for j in CurSet:
#         if j in ResDict:
#             # print('j=', j, 'ResDict[j]=', ResDict[j]) #.items())
#             CurSet = CurSet.union(ResDict[j])
#             # print('CurSet=', CurSet)
#     ResDict[CurKey] = ResDict[CurKey].union(CurSet)
#     # ResDict.setdefault(CurKey, set(CurSet) if len(inStr) > 1 else {CurKey})
# print('1-', *ResDict.items(), sep='\n', end='\n')
# for k, v in ResDict.items():
#     for elset in v:
#         if elset in ResDict:
#             # print('j=', j, 'ResDict[j]=', ResDict[j])  # .items())
#             ResDict[k] = ResDict[k].union(ResDict[elset])
#             # print('CurSet=', CurSet)
#
# # print('2-',*ResDict.items(), sep='\n', end='\n')
# for i in range(int(input())):
#     inStr = list(input().split())
#     predok = inStr[0]
#     potomok = inStr[1]
#     if predok in ResDict[potomok] or predok == potomok:
#         print('Yes')
#         # pass
#     else:
#         print('No')
#         # pass

# 1.6 Наследование классов 7 из 9 шагов пройдено
# ----------------------------------------------------------
# class ExtendedStack(list):
#     def sum(self):
#         self.append(self.pop() + self.pop())
#
#     def sub(self):
#         self.append(self.pop() - self.pop())
#
#     def mul(self):
#         self.append(self.pop() * self.pop())
#
#     def div(self):
#         self.append(self.pop() // self.pop())
# # ------------------------------------------------------------------
# class ExtendedStack(list):
#     def sum(self):
#         self[-2] = self[-1] + self[-2]
#         self.pop()
#
#
#     def sub(self):
#         self[-2] = self[-1] - self[-2]
#         self.pop()
#
#     def mul(self):
#         self[-2] = self[-1] * self[-2]
#         self.pop()
#
#     def div(self):
#         self[-2] = self[-1] // self[-2]
#         self.pop()
#
#
# def test():    #----------------------------------------------------------!!!!!
#     ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
#     ex_stack.div()
#     print(ex_stack)
#     print(ex_stack.pop() == 2)
#     print(ex_stack)
#     ex_stack.sub()
#     print(ex_stack)
#     print(ex_stack.pop() == 6)
#     ex_stack.sum()
#     print(ex_stack)
#     print(ex_stack.pop() == 7)
#     ex_stack.mul()
#     print(ex_stack)
#     print(ex_stack.pop() == 2)
#     print(len(ex_stack) == 0)
#
# test()

# 1.6 Наследование классов 8 из 9 шагов пройдено

# --------------------------------------------------------------
# class LoggableList(list, Loggable):
#     def append(self, x):
#         list.append(self, x)
#         self.log(x)
# --------------------------------------------------------------

# import time
# from contextlib import redirect_stdout
#
#
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))
#
#
# class LoggableList(list, Loggable):
#     def append(self, msg) -> None:
#         self.msg = msg  # self.log(msg)  # msg
#         super(LoggableList, self).append(self.msg)
#         super().log(self[-1])  # self.msg)  # super().log(msg=msg))
#
# gg = LoggableList()
# for i in range(5):
#     gg.append('----' + str(i) + '----')
