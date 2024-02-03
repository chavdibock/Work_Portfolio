// OOP_11.11.2022.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "Counter.h"
#include "Divider.h"
#include "Circle.h"
#include "Student.h"
#include "LongString.h"
#include "Point.h"
#include "BinarySearch.h"
using namespace std;
int main()
{/*

	double a, b;
	cin >> a >> b;
	Divider d(a, b);
   cout << d.result(a,b);

	////////////////////////////////////
	double r;
	cin >> r;
	Circle c(r);
	cout << c.getArea() << endl << c.getParameter() << endl << c.getRadius();
   */

   ////////////////////////////////////////////////
   /*
   const int size = 5;
   Circle arr[size] = { Circle(1), Circle(2),Circle(3) ,Circle(4) ,Circle(5) };
   Student array[size] = { Student("Pepi",100,100),
	   Student("Nikola",50,60),
	   Student("John",20,50),
	   Student("Gosho",10,25),
	   Student("Putex",40,90) };

   //sorting the array of students
   for (int i = 0; i < size - 1; i++) {
	   for (int j = 0; j < size - i - 1; j++) {
		   if (array[j].finalResult() < array[j + 1].finalResult())
		   {
			   swap(array[j], array[j+1]);
		   }
	   }

   }

   for (int i = 0; i < size; i++) {
	   cout << array[i].getName() << "The final result is " << array[i].finalResult() << endl;

   }

   */
   //////////////////////////////
   /*

   string  str = "test";
   LongString l(str);
   LongString l1(str);
	l.addString(l1);
	*/

	/////////////////////////////

	/*

   Point A(1,2);
   Point B(2,5);
   cout << A.calcDistance(B);

	*/

	BinarySerach s("11011");
	int Integer = s.convertToInteger();


	if (Integer == -1) {
		cout << "error";
	}
	else {

		cout << Integer;
	}

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
