#include"Product.h"
#include <iostream>
#include <string>

using namespace std;

Product::Product()
{
	name = "tea";
	quantity = 0;
	unitPrice = 0;
}

Product::Product(string n, double q, double p)
{
	name = n;
	quantity = q;
	unitPrice = p;
}

string Product::getName()
{
	return name;
}

void Product::setName(string n)
{
	name = n;
}

double Product::getQuantity()
{
	return quantity;
}

void Product::setQuantity(double q)
{
	if (q < 0) {
		cout << "Error";
	}
	else
	{
		quantity = q;
	}
}

double Product::getUnitPrice()
{
	return unitPrice;
}

void Product::setUnitPrice(double p)
{
	if (p < 0) {
		cout << "Error";
	}
	else
	{
		unitPrice = p;
	}
}

double Product::getTotalPrice()
{
	return getQuantity() * getUnitPrice();
}

void Product::display()
{
	// <name> <quantity> x <unitePrice>, so the price is: <the calculated price>.

	cout << getName() << " " << getQuantity() << " X " << getUnitPrice() << ", so the price is: " << getTotalPrice() << endl;
}
