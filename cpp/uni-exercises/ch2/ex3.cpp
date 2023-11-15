/* Write a C++ program that prompts the user to input the elapsed time for an event in hours, minutes, and seconds. The program then outputs the elapsed time in seconds. */

#include <iostream>

using namespace std;

int main()
{

    int hours, mins, seconds, result;

    cout << "Enter the elapsed time for an event in hours, minutes, and seconds: ";

    cin >> hours >> mins >> seconds;

    cout << "Elapsed time you entered: " << hours << ":" << mins << ":" << seconds << endl;

    mins = mins + (hours * 60);

    result = seconds + (mins * 60);

    cout << "The elapsed time in seconds: " << result;

    cout << endl;
    cin.get();
    cin.clear();

    return 0;
}

/* Professor solution:

#include <iostream>

using namespace std;

const int SECONDS_PER_HOUR = 3600;
const int SECONDS_PER_MINUTE = 60;

int main()
{
    int hours;
    int minutes;
    int seconds;

    cout << "Enter the hours of the elapsed time: ";
    cin >> hours;
    cout << endl;

    cout << "Enter the minutes of the elapsed time: ";
    cin >> minutes;
    cout << endl;

    cout << "Enter the seconds of the elapsed time: ";
    cin >> seconds;
    cout << endl;

    cout << "The elapsed time you entered is "
         << hours << ":" << minutes << ":" << seconds << endl;

    seconds = hours * SECONDS_PER_HOUR
              + minutes * SECONDS_PER_MINUTE
              + seconds;

    cout << "The equivalent time in seconds is "
         << seconds << endl;

    return 0;
}
 */