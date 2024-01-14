#include <iostream>

using namespace std;

int fibonacci(int p1, int p2, int n)
{
    int product = p1 + p2;

    if (n == 1)
        return p1;

    else if (n == 2)
        return p2;

    else
    {
        // int i = 3;

        // while (i <= n)
        // {
        //     product = p1 + p2;

        //     p1 = p2;
        //     p2 = product;

        //     i++;
        // }

        for (int i = 3; i <= n; i++)
        {
            product = p1 + p2;

            p1 = p2;
            p2 = product;
        }

        return product;
    }
}

int main()
{
    cout << fibonacci(1, 1, 15) << endl;
    cout << fibonacci(2, 3, 2) << endl;
    cout << fibonacci(5, 7, 1) << endl;
    cout << fibonacci(12, 16, 10) << endl;

    return 0;
}
