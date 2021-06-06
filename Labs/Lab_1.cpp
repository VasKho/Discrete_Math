#include <iostream>
#include "Test.h"

using namespace std;

int main()
{
    //Пользователь указывает способ задания множества
    cout << "Выберите способ задания множества (1 - Перечислительный; 2 - Высказывательный)" << endl;
    int ch;
    cin >> ch;
    Sets A, B;
    if (ch == 1)
    {
        A.enterSet(1, 'A');
        B.enterSet(1, 'B');
    }
    else if (ch == 2)
    {
        A.enterSet(2, 'A');
        B.enterSet(2, 'B');
    }
    Sets C = A.unite(B);
    Sets D = A.cross(B);
    Sets E = A.diff(B);
    Sets F = B.diff(A);
    Sets G = A.addition();
    Sets S = A.sym_diff(B);
    Sets H = A.cart_prod(B);
    cout << "Множество А:" << endl;
    A.print();
    cout << "Множество В:" << endl;
    B.print();
    cout << "Объединение:" << endl;
    C.print();
    cout << "Пересечение:" << endl;
    D.print();
    cout << "Разность А и В:" << endl;
    E.print();
    cout << "Разность В и А:" << endl;
    F.print();
    cout << "Дополнение А:" << endl;
    G.print();
    cout << "Симметрическая разность:" << endl;
    S.print();
    cout << "Декартово произведение А и В:" << endl;
    H.print();
    return 0;
}