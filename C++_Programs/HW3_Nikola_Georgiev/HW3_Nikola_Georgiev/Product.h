#pragma once
#include <string>
using namespace std;
class Product
{
public:
	Product();
	Product(string, double, double);
	string getName();
	void setName(string);
	double getQuantity();
	void setQuantity(double);
	double getUnitPrice();
	void setUnitPrice(double);
	double getTotalPrice();
	void display();


private:
	string name;
	double quantity;
	double unitPrice;

};