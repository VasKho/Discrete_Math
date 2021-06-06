import Graphics

# A = {(1, 1), (1, 3)}
# B = {(1, 2), (1, 3)}


# Ввод графика А
P1 = int(input('Введите количество пар в графике А: '))
A = set()
for i in range(P1):
    x1 = int(input('Введите первый элемент пары: '))
    y1 = int(input('Введите второй элемент пары: '))
    A.add((x1, y1))
print('A = ' + str(A))

# Ввод графика В
P2 = int(input('Введите количество пар в графике B: '))
B = set()
for i in range(P2):
    x2 = int(input('Введите первый элемент пары: '))
    y2 = int(input('Введите второй элемент пары: '))
    B.add((x2, y2))
print('B = ' + str(B))

# Операция объединения
C = Graphics.Union(A, B)
print('Объединение графиков А и В:\n' + str(C))
# Операция пересечения
D = Graphics.Cross(A, B)
print('Пересечение графиков А и В:\n' + str(D))
# Операция разности
E = Graphics.Differense(A, B)
print('Разность графиков А и В:\n' + str(E))
F = Graphics.Differense(B, A)
print('Разность графиков B и A:\n' + str(F))
# Операция симметрической разности
G = Graphics.Symmetric_Difference(A, B)
print('Симметрическая разность графиков А и В:\n' + str(G))
# Операция инвертирования
H = Graphics.Invert(A)
print('Инверсия графика А:\n' + str(H))
# Операция композиции
I = Graphics.Composition(A, B)
print('Композиция графиков А и В:\n' + str(I))
