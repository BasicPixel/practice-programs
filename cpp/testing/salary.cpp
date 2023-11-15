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

    double salary;
    double tax_rate = 0;
    double product;

    cout << "Enter a salary: ";
    cin >> salary;

    cout << "Enter the tax percentage: ";
    cin >> tax_rate;

    product = salary - (salary * (tax_rate / 100));

    cout << "Salary: " << salary << endl;
    cout << "Tax percentage: " << tax_rate << "%" << endl;
    cout << "Product: " << product << endl;

    return 0;
}
