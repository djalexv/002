# 1.1 Введение 9 из 10 шагов пройдено

# print(sum([int(input()) for _ in range(int(input()))]))

# def closest_mod_5(x: int):
# #     res = x
# #     while res % 5 != 0:
# #         res += 1
# #     return res
# # print(closest_mod_5(5))

# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res
#
# # print( s(11, 10))
# # print(s(11, b=20))
# # print(s(21))
# # print( s(5, 5, 5, 5, 1))
# print( s(11, 10, b=10))


# 1.3 Функции и стек вызовов 15 из 15 шагов пройдено
# ---------------------------------------
# n, k = 3, 2 #map(int, input().split())
# sz = max(n, k) + 1
# print(sz)
# c = [[0] * sz for _ in range(sz)]
# print(c)
#
# c[0][0] = 1
# print(c)
# for i in range(1, sz):
#     for j in range(i + 1):
#         c[i][j] = c[i - 1][j] + c[i - 1][j - 1]

# print(c)
# print(c[n][k])
# ----------------------------------------

# from itertools import combinations
# n, k = 3, 2 #map(int, input().split())
# print(sum(1 for _ in combinations(range(n), k)))


# def csh(_n: int, _k: int) -> int:
#     if _k == 0 or _n == _k:
#         return 1
#     elif _k > _n:
#         return 0
#     else:
#         return csh(_n-1, _k) + csh(_n - 1, _k-1)
#
#
# n, k = map(int, input().split())
# print(csh(n, k))


# 1.4 Пространства имён и области видимости 8 из 10 шагов пройдено

# x, y = 1, 2
#
# def foo():
#     global y
#     if y == 2:
#         x = 2
#         y = 1
#
# foo()
# print(x)
# if y == 1:
#     x = 3
# print(x)


# 1.4 Пространства имён и области видимости 9 из 10 шагов пройдено

# ---------------------------------------------
# info = dict({'global':[None]})
# def create(namespace, parent):
#     info.update({namespace:[parent]})
# def add(namespace, var):
#     info[namespace].append(var)
# def get(namespace, var):
#     while namespace != None and var not in info[namespace][1:]:
#         namespace = info[namespace][0]
#     print(namespace)
# operations = {'create': create, 'add': add, 'get': get} ------------!!!!!!!!!!!!!!!!!!!!!!!!
# for i in range(int(input())):
#     inp = input().split()
#     operations[inp[0]](inp[1], inp[2])   ------------------------!!!!!!!!!!!!!!!!!!!!!!

# for ops, nms, v in [input().split() for i in range(int(input()))]:   ---------------!!!!!!!!!

# ---------------------------------------------
#
#
# namespaces = {}
#
# def create(namespace, parent):
#     namespaces.update({namespace: {'parent': parent, 'vars': set()}})
#
#
# def add(namespace, var):
#     # assert isinstance(var, object)
#     namespaces[namespace]['vars'].add(var)
#
#
# def get(curentNameSpace, var):
#     resnm = ''
#     if curentNameSpace is None:
#         resnm = None
#     elif var in namespaces[curentNameSpace]['vars']:
#         resnm = curentNameSpace
#     else:
#         nn = namespaces[curentNameSpace]['parent']
#         resnm = get(namespaces[curentNameSpace]['parent'], var)
#     return resnm
#
#
# Result = []
# create('global', None)
# for i in range(int(input())):
#     instr = list(input().lower().split())
#     # map(instr[0])
#     if instr[0] == 'create':
#         create(instr[1], instr[2])
#     elif instr[0] == 'add':
#         add(instr[1], instr[2])
#     elif instr[0] == 'get':
#         Result.append((get(instr[1], instr[2])))
#     else:
#         pass
# # or i in f1:
# #     d[int(i.split()[0])].append(float(i.split()[2]))
#
#
# # add('global', 'var1')
# # add('global', 'var2')
# # add('global', 'var1')
# # create('newnm', 'global')
# # create('tttt', 'newnm')
# # add('newnm', 'x')
#
# # namespaces.update({'ff': {'parent': 'blobal', 'vars': []}})
# # print(*namespaces)
# print(*Result, sep='\n')
# # print('1-', get('global', 'var1'))
# # print('2-', get('tttt', 'x'))

# class Counter:
#     pass
#
# # Counter
# x = Counter()
# x.count = 0
# print(type (x))


