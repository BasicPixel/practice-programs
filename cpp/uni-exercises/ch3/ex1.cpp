/*
ExProg1: 	Write a program that prompts the user to enter the weight of a person in kilograms and outputs the equivalent weight in pounds. Output both the weights rounded to two decimal places. (Note that 1 kilogram = 2.2 pounds.) Format your output with two decimal places.
 */

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{

    double weightInKilos;
    cout << "Enter the weight in kilograms: ";
    cin >> weightInKilos;

    double weightInPounds = weightInKilos * 2.2;

    cout << fixed << showpoint << setprecision(2);

    cout << "Weight in kilos: " << weightInKilos << endl;
    cout << "Weight in pounds: " << weightInPounds << endl;

    cout
        << endl;
    cin.get();
    cin.clear();

    return 0;
}