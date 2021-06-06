# Задание множества
def Enter_Set(name, P, type_of_def):
    # Перечислительное задание множества
    if type_of_def == 1:
        A = set()
        for i in range(P):
            # Пользователь указывает элемент х
            x = int(input('Введите элемент множества: '))
            # Добавление элемента х в множество
            A.add(x)
    # Высказывательное задание множества
    elif type_of_def == 2:
        A = set()
        # Задание множества А
        if name == 'A':
            A = {5*i + 1 for i in range(P)}
        # Задание множества В
        else:
            A = {100 - i*i for i in range(P)}
    return A

# Объединение множеств
def Union(A, B):
    # Создаём новое множество
    # Записываем в него элементы из А
    Union = {i for i in A}
    b = False
    # Выбираем элемент из В
    for i in B:
        # Выбираем элемент из А
        for j in Union:
            # Сравниваем выбранные элементы
            # Если они равны, то переходим к следующему элементу из В
            if i == j:
                b = True
                break
        if b == False:
            Union.add(i)
        else:
            b = False
    return Union

# Пересечение множеств
def Cross(A, B):
    # Создаём новое множество
    Cross = set()
    # Выбираем элемент из А
    for i in A:
        # Выбираем элемент из В
        for j in B:
            # Сравниваем выбранные элементы
            # Если они равны, то добавляем один их них в новое множество
            if i == j:
                Cross.add(i)
    return Cross

# Разность множеств
def Differense(A, B):
    # Создаём новое множество
    Differense = set()
    b = False
    # Выбираем элемент из А
    for i in A:
        # Выбираем элемент из В
        for j in B:
            # Сравниваем выбранные элементы
            if i == j:
                b = True
                break
        if b == False:
            Differense.add(i)
        else:
            b = False
    return Differense

# Симметрическая разность множеств
def Symmetric_Difference(A, B):
    # Создаём новое множество
    Symmetric_Difference = set()
    # Находим разность множеств А и В
    Temp1 = Differense(A, B)
    # Находим разность множеств В и А
    Temp2 = Differense(B, A)
    # Объединяем полученные множества
    Symmetric_Difference = Union(Temp1, Temp2)
    return Symmetric_Difference

# Дополнение множества
def Addition(A):
    # Объявляем универсум и заполняем его элементами 0,1,...,100
    U = {i for i in range(101)}
    # Находим разность универсума и множества
    Addition = Differense(U, A)
    return Addition

# Декартово произведение
def Cartesian_Product(A, B):
    # Создаём новое множество
    C_P = set()
    # Выбираем элемент i из А
    for i in A:
        # Выбираем элемент k из В
        for k in B:
            # Добавляем пару <i, k> в новое множество
            C_P.add((i, k))
    return C_P
