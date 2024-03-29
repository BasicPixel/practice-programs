#include <iostream>
using namespace std;

int main()
{
    int firstvalue = 5, secondvalue = 15;
    int *p1, *p2;

    p1 = &firstvalue;  // p1 = address of firstvalue
    p2 = &secondvalue; // p2 = address of secondvalue

    cout << "p1: " << p1 << "\n";
    cout << "p2: " << p2 << "\n";
    cout << "firstvalue: " << firstvalue << "\n";
    cout << "secondvalue: " << secondvalue << "\n";

    p1 = p2;

    cout << "-----\n\n";

    cout << "p1: " << p1 << "\n";
    cout << "p2: " << p2 << "\n";
    cout << "firstvalue: " << firstvalue << "\n";
    cout << "secondvalue: " << secondvalue << "\n";

    *p1 = 10;
    *p2 = *p1;
    p1 = p2;
    *p1 = 20;

    cout << "-----\n\n";

    cout << "p1: " << p1 << "\n";
    cout << "p2: " << p2 << "\n";
    cout << "firstvalue: " << firstvalue << "\n";
    cout << "secondvalue: " << secondvalue << "\n";

    cout << "-----\n\n";

    // value pointed to by p1 = 10
    // value pointed to by p2 = value pointed to by p1
    // p1 = p2 (value of pointer is copied)
    // value pointed to by p1 = 20
    // cout << "firstvalue is " << firstvalue << '\n';
    // cout << "secondvalue is " << secondvalue << '\n';

    return 0;
}