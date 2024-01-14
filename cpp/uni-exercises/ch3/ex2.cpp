/*
ExProg2: Write a program that accepts as input the mass, in grams, and density, in grams per cubic centimeters, and outputs the volume of the object using the formula: density ¼ mass / volume. Format your output to two decimal places.
 */

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    double mass;
    double density;
    double volume;

    cout << fixed << showpoint << setprecision(2);

    cout << "the mass, in grams: ";
    cin >> mass;

    cout << "the density, in grams per cubic centimeters: ";
    cin >> density;

    volume = mass / density;

    cout << volume;

    cout
        << endl;
    cin.get();
    cin.clear();

    return 0;
}