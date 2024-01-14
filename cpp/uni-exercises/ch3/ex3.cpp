/*
    ExProg3:

    Write a program that calculates and prints the monthly paycheck for an employee. The net pay is calculated after taking the following deductions:
    Federal Income Tax: 15%
    State Tax: 3.5%
    Social Security Tax: 5.75%
    Medicare/Medicaid Tax: 2.75%
    Pension Plan: 5%
    Health Insurance: $75.00

    Your program should prompt the user to input the gross amount and the employee name. Format your output to have two decimal places. A sample output follows:

    Bill Robinson
    Gross Amount: ............ $3575.00
    Federal Tax: ............. $ 536.25
    State Tax: ............... $ 125.13
    Programming Exercises | 173
    Social Security Tax: ..... $ 205.56
    Medicare/Medicaid Tax: ... $ 98.31
    Pension Plan: ............ $ 178.75
    Health Insurance: ........ $ 75.00
    Net Pay: ................. $2356.00
    Note that the first column is left justified, and the right column is right justified

 */

#include <iostream>
#include <string>
#include <iomanip>

const double FEDERAL_TAX_RATE = 0.15;
const double STATE_TAX_RATE = 0.035;
const double SOCIAL_SECURITY_TAX_RATE = 0.0575;
const double MEDICARE_MEDICATE_TAX_RATE = 0.0275;
const double PENSION_PLAN_RATE = 0.05;
const double HEALTH_INSURANCE = 75.00;

using namespace std;

int main()
{
    string name;

    double grossAmount;
    double federalTax;
    double stateTax;
    double socialSecurityTax;
    double medicareMedicaidTax;
    double pensionContribution;
    double netPay;

    cout << "Enter the employee name: ";
    getline(cin, name);
    cout << endl;

    cout << "Enter gross amount: ";
    cin >> grossAmount;
    cout << endl;

    federalTax = grossAmount * FEDERAL_TAX_RATE;
    stateTax = grossAmount * STATE_TAX_RATE;
    socialSecurityTax = grossAmount * SOCIAL_SECURITY_TAX_RATE;
    medicareMedicaidTax = grossAmount * MEDICARE_MEDICATE_TAX_RATE;
    pensionContribution = grossAmount * PENSION_PLAN_RATE;

    netPay = grossAmount - federalTax - stateTax -
             socialSecurityTax - medicareMedicaidTax -
             pensionContribution - HEALTH_INSURANCE;

    cout << name << endl;

    cout << left << setw(26) << setfill('.') << "Gross amount: " << right << setfill(' ') << "$" << setw(7) << grossAmount << endl;
    cout << left << setw(26) << setfill('.') << "Gross amount: " << right << setfill(' ') << "$" << setw(7) << grossAmount << endl;
    cout << left << setw(26) << setfill('.') << "Gross amount: " << right << setfill(' ') << "$" << setw(7) << grossAmount << endl;
    cout << left << setw(26) << setfill('.') << "Gross amount: " << right << setfill(' ') << "$" << setw(7) << grossAmount << endl;

    cout
        << endl;
    cin.get();
    cin.clear();

    return 0;
}