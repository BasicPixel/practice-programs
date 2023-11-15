#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main()
{
    double value, *address;

    value = 8.8;

    address = &value;

    cout << "----------";

    cout
        << "Value: " << value;
    cout << "\n";
    cout << "Address: " << address;
    cout << "\n";

    return 0;
}
