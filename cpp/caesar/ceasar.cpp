#include <iostream>

using namespace std;
// #include <string.h>

string caesar(string str)
{
    return str;
}

int main(int argc, char const *argv[])
{
    string str;

    if (argc < 2)
    {
        cout << "Enter a string: ";
        cin >> str;
    }
    else
    {
        // str = argv[2];
        // cout << argv[1];
        // cout << argv[2];
    }

    cout << str;

    return 0;
}