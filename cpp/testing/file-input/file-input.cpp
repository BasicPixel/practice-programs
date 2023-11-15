/*
    This is a C++ Program
    For Computer Skills for Scientific Faculties class.
*/

#include <string>
#include <fstream>

using namespace std;

int main()
{

    string stno;
    string name;

    ifstream infile("input.txt");
    ofstream outfile("output.txt", ios::app);

    infile >> stno;
    getline(infile, name);

    outfile << "Name: " << name << "\t"
            << "Number: " << stno << endl;

    infile.close();
    outfile.close();

    return 0;
}