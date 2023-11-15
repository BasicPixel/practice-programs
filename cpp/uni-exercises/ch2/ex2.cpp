/* Write a program that prompts the user to input five decimal numbers.The
    program should then add the five decimal numbers,
    convert the sum to the
        nearest integer,
    and print the result.
 */

#include <iostream>

using namespace std;

int main()
{

    double n1, n2, n3, n4, n5;

    cout << "Enter 5 decimal numbers: ";

    cin >> n1 >> n2 >> n3 >> n4 >> n5;

    // Added 0.5 as a trick to round when casting to integer
    int sum = static_cast<int>(n1 + n2 + n3 + n4 + n5 + 0.5);

    cout << "Sum rounded to nearest integer: " << sum;

    cout << endl;
    cin.get();
    cin.clear();

    return 0;
}
