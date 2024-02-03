#include <iostream>
#include <string>
#include"Product.h"
#include "Category.h"
#include"Service.h"
#include <vector>
using namespace std;

int main()
{   //initializing vectors
	vector<Category*> arrCategory;
	vector<Product*> arrProduct;
	vector<Service*> arrService;
	vector <Item*> arrItem;
	
	//initializing Categories
	Category Tech("Technology", "a1", "makes things", NULL);
	Category Pharmacy("Pharmacy", "b1", "makes things", NULL);
	Category Vehicle("HealthCare", "c1", "makes things", NULL);
	arrCategory.push_back(&Tech);
	arrCategory.push_back(&Pharmacy);
	arrCategory.push_back(&Vehicle);

	//initializing Products
	Product Router("Router", "rt1", "description of the product", 1000, 50.0, &Tech, 1, percentage);
	Product Nurophen("Nurophen", "nrph", "description of the product", 10, 10, &Pharmacy, 1, percentage);
	Product Farrai("Ferrari", "ferrari", "description of the product", 100000, 5, &Vehicle, 1, percentage);

	arrItem.push_back(&Router);
	arrItem.push_back(&Nurophen);
	arrItem.push_back(&Farrai);

	//initializing Products
	Service RouterService("RouterService", "rt1-service", "description of the product", 100, 25, &Tech, 1, percentage, 5, 85, 3, percentage_);
	Service NurophenDelivery("NurophenDelivery", "nrph-deli", "description of the product", 5, 0, &Pharmacy, 1, percentage, 2, 4, 0, percentage_);
	Service TireReplacement("TireReplacement", "ferrari-main", "description of the product", 1000, 50.0, &Vehicle, 1, percentage, 8, 850, 10, percentage_);
	
	arrItem.push_back(&RouterService);
	arrItem.push_back(&NurophenDelivery);
	arrItem.push_back(&TireReplacement);


	string pat = "Ro";

	for (int i = 0; i < arrItem.size(); i++)
	{
		arrItem[i]->KPM(pat);

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
