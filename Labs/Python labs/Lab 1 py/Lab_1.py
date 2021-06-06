import Sets

# Пользователь указывае тспособ задания множеств
type_def = int(input('Выберите способ задания множества:\n1 - перечислительный;\n2 - высказывательный.\n'))
# Пользователь указывает мощность множества А
P1 = int(input('Введтие мощность множества A (<= 10): '))
# Задание множества А
A = Sets.Enter_Set('A', P1, type_def)
# Пользователь указывает мощность множества В
P2 = int(input('Введтие мощность множества B (<= 10): '))
# Задание множества В
B = Sets.Enter_Set('B', P2, type_def)

print('Множество А:')
print('A = ' + str(A))
print('Множество B:')
print('B = ' + str(B))
# Операция объединения
C = Sets.Union(A, B)
print('Объединение А и В:')
print(C)
# Операция пересечения
D = Sets.Cross(A, B)
print('Пересечение А и В:')
if len(D) == 0:
    print('{}')
else:
    print(D)
# Операция Разности
E = Sets.Differense(A, B)
print('Разность А и В:')
print(E)

I = Sets.Differense(B, A)
print('Разность B и A:')
print(I)
# Дополнение множества
F = Sets.Addition(A)
print('Дополнение А:')
print(F)
# Симметрическая разность
G = Sets.Symmetric_Difference(A, B)
print('Симметрическая разность А и В:')
print(G)
# Декартово произведение
H = Sets.Cartesian_Product(A, B)
print('Декартово произведение А на В')
print(H)
J = Sets.Cartesian_Product(B, A)
print('Декартово произведение B на A')
print(J)