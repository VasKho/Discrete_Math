import Sets
import Graphics

def Enter ():
    X = set()
    Px = int(input('Введите мощность области отправления: '))
    for i in range(Px):
        x = int(input('Введите элемнент x области отправления: '))
        X.add(x)
    Y = set()
    Py = int(input('Введите мощность области прибытия: '))
    for k in range(Py):
        y = int(input('Введите элемнент y области прибытия: '))
        Y.add(y)
    F = set()
    Pf = int(input('Введите мощность графика соответствия: '))
    for i in range(Pf):
        x1 = int(input('Введите первый элемент пары: '))
        y1 = int(input('Введите второй элемент пары: '))
        F.add((x1, y1))
    A = (X, Y, F)
    return A

def union (A, B):
    U1 = Sets.Union(A[0], B[0])
    U2 = Sets.Union(A[1], B[1])
    U3 = Graphics.Union(A[2], B[2])
    U4 = (U1, U2, U3)
    return U4

def cross(A, B):
    C1 = Sets.Cross(A[0], B[0])
    C2 = Sets.Cross(A[1], B[1])
    C3 = Graphics.Cross(A[2], B[2])
    C4 = (C1, C2, C3)
    return C4

def differense(A, B):
    D1 = Sets.Differense(A[0], B[0])
    D2 = Sets.Differense(A[1], B[1])
    D3 = Graphics.Differense(A[2], B[2])
    D4 = (D1, D2, D3)
    return D4

def symmetric_differense(A, B):
    S1 = Sets.Symmetric_Difference(A[0], B[0])
    S2 = Sets.Symmetric_Difference(A[1], B[1])
    S3 = Graphics.Symmetric_Difference(A[2], B[2])
    S4 = (S1, S2, S3)
    return S4

def inversion(A):
    I = Graphics.Invert(A[2])
    Ai = (A[1], A[0], I)
    return Ai

def composition(A, B):
    C1 = Graphics.Composition(A[2], B[2])
    C = (A[0], B[1], C1)
    return C

def constriction(A):
    Pс = int(input('Введите мощность множества для сужения: '))
    X = set()
    for i in range(Pс):
        x = int(input('Введите элемнент x множества для сужения: '))
        X.add(x)
    C_P = Sets.Cartesian_Product(X, A[1])
    Cr = Graphics.Cross(A[2], C_P)
    Con = (A[0], A[1], Cr)
    return Con

def continues(A):
    N = set()
    Pn = int(input('Введите мощность графика: '))
    for i in range(Pn):
        x1 = int(input('Введите первый элемент пары: '))
        y1 = int(input('Введите второй элемент пары: '))
        N.add((x1, y1))
    for k in A[2]:
        eq = 0
        for i in N:
            if k == i:
                eq = 1
                break
        if eq == 0:
            return False
    print('Соответствие ' + str((A[0], A[1], N)) + ' является продолжением:\n')
    return True
       
def imaginire(A):
    Res = set()
    Pi = int(input('Введите мощность множества для образа: '))
    I = set()
    for i in range(Pi):
        x = int(input('Введите элемнент x множества для образа: '))
        I.add(x)
    for i in I:
        for k in A[2]:
            if k[0] == i:
                Res.add(k[1])
    return Res

def neg_imaginire(A):
    Res = set()
    Pi = int(input('Введите мощность множества для прообраза: '))
    I = set()
    for i in range(Pi):
        x = int(input('Введите элемнент x множества для прообраза: '))
        I.add(x)
    for i in I:
        for k in A[2]:
            if k[1] == i:
                Res.add(k[0])
    return Res

