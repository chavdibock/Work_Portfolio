// HW3_Nikola_Georgiev.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include "Product.h"
using namespace std;


int main()
{
	ifstream ins;
	//openning the file
	ins.open("D:/AUBG/COS_Major/COS_120_EMANUELA_MITREVA_FALL_2022 - Copy/Progaming_problems/HW3_Nikola_Georgiev/Products.txt");

	if (ins.fail()) {     // check if there was an error
		cout << "Error opening file";
		return -1;
	}
	double totalPrice = 0;
	string productName = "";
	double quan =0;
	double price = 0;

	while (!ins.eof())
	{
		// Reading until the specifhic symbul
		getline(ins, productName, '$');
		ins >> quan >> price;
		ins.ignore(1, '\n');
		Product p(productName,quan,price); // Initializing the constructor.
		totalPrice += p.getTotalPrice();
		p.display(); // Displaying the total price
	
	}
	

	ins.close();


	//Displaiyng the total amount ot be paid
	cout <<endl <<"The total amount we have to pay is " << totalPrice << " .";




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
