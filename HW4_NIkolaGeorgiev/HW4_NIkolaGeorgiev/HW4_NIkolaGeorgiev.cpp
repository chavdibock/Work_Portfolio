// HW4_NIkolaGeorgiev.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "Book.h"

#include"ChildrenBook.h"

#include "SeriousBook.h"
using namespace std;
int main()
{
    Book s("Gosho", "NIkola", 12);
    ChildrenBook s1("Gosho", "NIkola", 12, 13);
    Book s2("Gosho", "NIkola", 13);
    SeriousBook a("georgie", "ivan", 23, "fantasy");
    ChildrenBook b;
   
   
    //console input       
    cin >> b;


    cout << b.getName() << endl;
    cout << b.getAuthor() << endl;
    cout << b.getPages() << endl;
    cout << b.getAgeAppropriate() << endl;
     

    //equality operator
    if (s2 == b) {
        cout << "same";
    }
    else {
        cout << "not";
    }
   
   
    //virtual function
    s.type();
    s1.type();
    a.type();   

    
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
