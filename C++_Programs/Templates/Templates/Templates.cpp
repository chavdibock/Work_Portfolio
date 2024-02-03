// Templates.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include "Person.h"
using namespace std;
/*
Define a void function called applyVAT which takes a variable containing a product’s price and adds
20% tax to it.
*/

double applyVAT(double a) {
    return a += a * .2;
}


/*
Define the definition of a class named Person, which has two private members – name and age.
Declare three constructors for the class – default constructor, two-parameter constructor and the copy
constructor. Declare a destructor for that class.   
*/



/*
Define a class called Student which has three attributes – name, exams and quizzes. Add three-
parameter constructor.
Add a member function called getFinalGrade, which calculates and returns the final grade of the
student as a number between 0 and 100, where quizzes make 40% and exams make 60% of that grade.
Add a method called displayGrade, which calls getFinalGrade above and outputs the
corresponding letter for the final grade of the student. Use the following grade scale: 0-60 (F), 61-70
(D), 71-80 (C), 81-90 (B), and 91-100 (A).
Override the less than operator (operator<) that is checking whether the left operand’s final grade is
less than the right operand’s final grade.
Write a main function to create an instance of the Student class and call the displayGrade
method.
*/




int main()
{/*
 
    double vat = 100;
    cout << applyVAT(vat);
    
    /////////////////////

    Person t;
    Person a("Nikola", 15);
    cout << t.getAge()<< endl<< t.getName()<<endl
        << a.getAge() << endl << a.getName();
   
   */
   
   
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
