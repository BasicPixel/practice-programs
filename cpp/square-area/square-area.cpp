#include <iostream>

using namespace std;

int main()
{
	cout << "Hello, world!\n\n";

	float height, width;

	cout << "Height: ";
	cin >> height;

	cout << "Width: ";
	cin >> width;

	float answer = height * width;

	cout << "Area = " << answer << "\n\n";

	return 0;
}