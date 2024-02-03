// Final.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "Contact.h"
#include "DiaryProduct.h"
#include <string>
using namespace std;

template <class Object>
bool foo(Object& lhs, Object& rhs)
{
    if (lhs != rhs) {
        return true;
    }
    else {
        return false;
    }
       
}

int main()
{//Ex1

    /*
    
    int a = 0;
    int b = 0;
    if (foo(a,b)==true) {
        cout << "true";
    }
    else
    {
        cout << "false";

    }

    */

    /*
    
   
    string n = "Gosho";
    string a = "Blago";
    Contact c;
    Contact c1(n,a);
    Contact c2(c1);

     */

    DiaryProduct c;
    cout << c.getName() << endl << c.getPrice();
    return 0;
    
    }

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
