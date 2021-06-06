#pragma once
#ifndef _SETS_H_
#define _SETS_H_
#include <cstddef>
#include <iostream>
#include <math.h>
class Sets
{
private:
    int* A;
    int** C;
    int short p = 0;
    bool contains(int);
    void add();                     //Задание перечислением
public:
    void enterSet(int, char);       //Задание множеств
    void print();
    Sets unite(Sets, int = 0);      //Объединение множеств
    Sets cross(Sets);               //Пересечение множеств
    Sets diff(Sets);                //Разность множеств
    Sets sym_diff(Sets);            //Симметрическая разность
    Sets addition();                //Дополнение
    Sets cart_prod(Sets);           //Декартово произведение
};

bool Sets::contains(int item)               //Проверка наличия элемента во множестве
{
    int i = 0;
    while (i < p) {if (A[i] == item) return true;
    i++;}
    return false;
}

void Sets::add()                            //Ввод множества перечислением
{
    std::cout << "Введите мощность множества: ";
    /*   Пользователь указывает мощность множества   */
    std::cin >> p;
    A = new int[p];
    int short k = 0;
    int x;
    /*   Проверка повторяющихся элементов   */
    while (k < p)
    {
        bool b = 0;
        /*   Пользователь указывает элемент х   */
        std::cin >> x;
        if (!contains(x)) A[k++] = x;
    }
}

void Sets::enterSet(int ch, char exp)       //Ввод множества
{
    /*   Если выбран перечислительный способ,
    то вызываем соответствующую функцию   */
    if (ch == 1)
    {
        add();
        return;
    }
    /*   Если выбран высказывательный способ   */
    else if (ch == 2)    
    {
        /*   Задание множества А   */
        if (exp == 'A')
        {
            int P1;
            std::cout << "Введите  мощность множества А (<= 10): ";
            std::cin >> P1;
            int k = 1;
            while (5*k+1 < 101 && 5*k+1 >= 0 && k <= P1) {p++; k++;}
            A = new int[p];
            k = 1;
            while (5*k+1 < 101 && k <= P1) 
            {
                A[k-1] = 5*k+1;
                k++;
            }
        }
        /*   Задание множества В   */
        else if (exp == 'B')
        {
            int P2;
            std::cout << "Введите  мощность множества B (<= 10): ";
            std::cin >> P2;
            int k = 1;
            while (100-k*k < 101 && 100-k*k >= 0 && k <= P2) {p++; k++;}
            A = new int[p];
            k = 1;
            while (100-k*k < 101 && 100-k*k >= 0 && k <= P2)
            {
                A[k-1] = 100-k*k;
                k++;
            }
        }
    }
    else return;
}

void Sets::print()                          //Вывод множества
{
    int i = 0;
    if (!this->A)
    {
        while (i < p) 
        {
            printf("(%d, %d) ", this->C[i][0], this->C[i][1]);
            i++;
        }
        std::cout << std::endl;
    }
    else
    {
        while (i < p) std::cout << A[i++] << " ";
        std::cout << std::endl;
    }
}

Sets Sets::unite(Sets B, int sym)           //Объединение
{
    bool b = false;
    int p_u = this->p, cur_p = this->p;     //p_u - мощность объединения, cur_p - счётчик для элементов объединения
    if (sym == 1) 
    {
        p_u = this->p + B.p;
        goto skip;
    }
    /*   Двумя циклами проверяем элементы двух множеств и
    при нахождении неповторяющегося элемента увеличиваем 
    мощность объединения на 1   */
    for (int k = 0; k < B.p; k++)
    {
        for (int i = 0; i < this->p; i++)
        {
            if (B.A[k] == this->A[i]) {b = true; break;}
        }
        if (!b) p_u++;
        else b = false;
    }
   // p_u++;
skip:
    Sets C;
    C.p = p_u;
    b = false;
    C.A = new int[p_u];
    //Добавляем элементы множества А в множество С
    for (int i = 0; i < this->p; i++) C.A[i] = this->A[i];
    int k = 0;
    while (k < B.p)       //Пока счётчик k меньше мощности множества B
    {
        int i = 0;
        while (i < this->p)       //Пока счётчик i меньше мощности множества A
        {
            if (C.A[i] == B.A[k]) {b = true; break;}
            i++;
        }
        /*   Если совпадений не найдено, то добавляем 
        k-ый элемент множества B в объединение   */
        if (!b) C.A[cur_p++] = B.A[k];
            else b = false;
        k++;
    }
    return C;
}

Sets Sets::cross(Sets B)                    //Пересечение
{
    /*   Поиск мощности пересечения   */
    int short i = 0, k = 0;
    int p_c = 0;
    /*   Если в множестве В есть i-ый элемент множества А,
    то увеличиваем мощность пересечения на 1   */
    while (i < p) if (B.contains(A[i++])) p_c++;
    Sets cross;
    cross.A = new int[p_c];
//    cross.A = (int*)malloc(p_c * sizeof(int));
    cross.p = p_c;
    i = 0;
    /*   Если в множестве В есть i-ый элемент множества A,
    то добавляем его в пересечение   */
    while (i < p) 
    {
        if (B.contains(A[i])) cross.A[k++] = A[i];
        i++;
    }
    return cross;
}

Sets Sets::diff(Sets B)                     //Разность
{
    Sets C;
    /*   Поиск мощности разности   */
    int i = 0, j = 0;
    while (i < p)
    {
        int k = 0;
        bool b = false;
        /*   Если i-ый элемент множества А не принадлежит
        множеству В, то увеличиваем мощность разности на 1   */
        while (k < B.p)
        {
            if (A[i] == B.A[k]) {b = true; break;}
            k++;
        }
        if (!b) C.p++;
        i++;
    }
    i = 0;
    C.A = new int[C.p];
    while (i < p)
    {
        int k = 0;
        bool b = false;
        /*   Если i-ый элемент множества А не принадлежит
        множеству В, то добавляем его в разность   */
        while (k < B.p)
        {
            if (A[i] == B.A[k]) {b = true; break;}
            k++;
        }
        if (!b) C.A[j++] = A[i];
        i++;
    }
    return C;
}

Sets Sets::sym_diff(Sets B)                 //Симметрическая разность
{
    Sets C, D;
    C = this->diff(B);      //Разность множеств А и В
    D = B.diff(*this);      //Разность множеств В и А
    return C.unite(D, 1);   //Объединение двух разностей
}

Sets Sets::addition()                       //Дополнение
{
    Sets U;
    U.p = 101;
    U.A = new int[U.p];
    for (int i = 0; i <= 100; i++) U.A[i] = i;
    return U.diff(*this);           //Находим разность универсума и множества А
}

Sets Sets::cart_prod(Sets B)                //Декартово произведение
{
    Sets C;
    C.A = NULL;
    /*   Определяем количество пар в произведении   */
    C.p = this->p * B.p;
    C.C = new int*[C.p];
    for (int i = 0; i < C.p; i++) C.C[i] = new int[2];
    int i = 0, j = 0;
    while (i < this->p)
    {
        int k = 0;
        /*   Составляем пару из i-ого элемента множества А и
        k-ого элемента множества В; Добавляем её в множество произведения*/
        while (k < B.p)
        {
            C.C[j][0] = this->A[i];
            C.C[j][1] = B.A[k];
            j++;
            k++;
        }
        i++;
    }
    return C;
}
#endif