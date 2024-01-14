/* Q4: A milk carton can hold 3.78 liters of milk. Each morning, a dairy farm ships cartons of milk to a local grocery store. The cost of producing one liter of milk is $0.38, and the profit of each carton of milk is $0.27. Write a program that does the following:
2
a)	Prompts the user to enter the total amount of milk produced in the morning.
b)	Outputs the number of milk cartons needed to hold milk. (Round your answer to the nearest integer.)
c)	Outputs the cost of producing milk.
d)	Outputs the profit for producing milk.
 */

#include <iostream>

const double CARTON_CAPACITY = 3.78;

using namespace std;

int main()
{

    /*  */
    double milk_amount;
    cout << "Enter the amount of milk in liters: ";
    cin >> milk_amount;

    int cartons = static_cast<int>(milk_amount / CARTON_CAPACITY + 0.5);
    double cost = milk_amount * 0.38;
    double profit = cartons * 0.27;

    cout << "Number of cartons: " << cartons << endl;
    cout << "Cost: " << cost << endl;
    cout << "Profit: " << profit << endl;

    cout << endl;
    cin.get();
    cin.clear();

    return 0;
}