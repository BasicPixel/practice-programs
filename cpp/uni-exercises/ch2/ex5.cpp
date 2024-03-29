/* Q5: Newton’s law states that the force, F, between two bodies of masses M_1and M_2 is given by:

F=k((M_1 M_2)/d^2 )
in which k is the gravitational constant and d is the distance between the bodies. The value of k is approximately 6.67*〖10〗^(-8) dyn. cm2/g2. Write a program that prompts the user to input the masses of the bodies and the distance between the bodies. The program then outputs the force between the bodies.

 */

#include <iostream>

using namespace std;

const double GRAVITATIONAL_CONSTANT = 6.67 / 100000000;

int main()
{

    double m1, m2, d;

    cout << "Enter the mass of the first body: ";
    cin >> m1;

    cout << "Enter the mass of the second body: ";
    cin >> m2;

    cout << "Enter the distance between the two bodies: ";
    cin >> d;

    double f = GRAVITATIONAL_CONSTANT * ((m1 * m2) / (d * d));

    cout << "Force: " << f;

    cout
        << endl;
    cin.get();
    cin.clear();

    return 0;
}