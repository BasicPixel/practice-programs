/*
    This is a C++ Program
    For Computer Skills for Scientific Faculties class.
*/

#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int main()
{

    string str1 = "Osama", str2 = "Hello";

    cout << "Bitwise operators\n";

    // AND, compares bits
    cout << (9 & 12) << "\n";

    // XOR
    cout << (9 ^ 12) << "\n";

    // OR
    cout << (9 | 12) << "\n";

    // Left shift
    cout << (9 << 1) << "\n";
    cout << (9 << 2) << "\n";
    cout << (9 << 3) << "\n";

    // Right shift
    cout << (9 >> 1) << "\n";

    // 1 becomes 0 and vice versa, adds 1 and makes it negative
    cout << (~9) << "\n";

    return 0;
}
