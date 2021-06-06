# Объединение графиков
def Union(A, B):
    # Создаём новый график
    # Записываем в него элементы из А
    Union = {(i[0], i[1]) for i in A}
    b = False
    # Выбираем элемент из В
    for i in B:
        # Выбираем элемент из А
        for j in Union:
            # Сравниваем выбранные пары
            # Если они равны, то переходим к следующему элементу из В
            if i == j:
                b = True
                break
        if b == False:
            Union.add(i)
        else:
            b = False
    return Union

# Пересечение графиков
def Cross(A, B):
    # Создаём новый график
    Cross = set()
    # Выбираем элемент из А
    for i in A:
        # Выбираем элемент из В
        for j in B:
            # Сравниваем выбранные пары
            # Если они равны, то добавляем одну их них в новый график
            if i == j:
                Cross.add(i)
    return Cross

# Разность графиков
def Differense(A, B):
    # Создаём новый график
    Differense = set()
    b = False
    # Выбираем элемент из А
    for i in A:
        # Выбираем элемент из В
        for j in B:
            # Сравниваем выбранные пары
            if i == j:
                b = True
                break
        if b == False:
            Differense.add(i)
        else:
            b = False
    return Differense

# Симметрическая разность графиков
def Symmetric_Difference(A, B):
    # Создаём новый график
    Symmetric_Difference = set()
    # Находим разность графиков А и В
    Temp1 = Differense(A, B)
    # Находим разность графиков В и А
    Temp2 = Differense(B, A)
    # Объединяем полученный графики
    Symmetric_Difference = Union(Temp1, Temp2)
    return Symmetric_Difference

# Инверсия графика
def Invert(A):
    # Создаём новый график
    # Выбираем пару из А
    # Меняем её элементы местами
    # Добавляем её в новый график 
    Inverted = {(i[1], i[0]) for i in A}
    return Inverted

# Композиция графиков
def Composition(A, B):
    # Создаём новый график
    Composition = set()
    # Выбираем элемент из графика А
    for i in A:
        # Выбираем элемент из графика В
        for j in B:
            # Сравниваем вторую компоненту пары из графика А
            # с первой компонентой пары из графика В 
            if i[1] == j[0]:
                # Если они равны, то добавляем в новый график пару из первой
                # компоненты пары из графика А и второй компоненты из графика В
                Composition.add((i[0], j[1]))
    return Composition