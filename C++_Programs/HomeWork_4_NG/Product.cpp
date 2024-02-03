#include "Product.h"
#include "Category.h"
#include <iostream>
#include <vector>
using namespace std;



Product::Product(string name, string tKey, string decrp, double prc, double dsc, Category* ctgr, int quant, DiscountType dscType) : Item(name,tKey)
{
	//using setters for the constructor

	setDescription(decrp);
	setPrice(prc);
	setDiscount(dsc);
	setCategory(ctgr);
	setQuantity(quant);
	setDiscountType(dscType);
}

//implementing setters and getters
void Product::setQuantity(int a)
{
	if (a < 0) {
		cerr << "The quantity  cannot be negative\n";
		exit(1);
	}
	else
	{
		this->Quantity = a;
	}
}

void Product::setPrice(double pr)
{
	if (pr < 0) {
		cout << "Invalid input of the price parameter for product " << getName() << "\n";
		exit(1);
	}
	else
	{
		this->price = pr;
	}
}

void Product::setDiscount(double dsc)
{
	if (dsc < 0 ) {
		cout << "Invalid input of the discount parameter for product " << getName() << "\n";
		exit(1);
	}
	else
	{
		this->Discount = dsc;
	}
}

DiscountType Product::getDiscountType()
{
	return this->type;
}

void Product::setDiscountType(DiscountType a)
{
	if (a == percentage || a == amount) {

		this->type = a;
	}
	else {
		cout << "Invalid discount type!!!\n";
		exit(1);

	}
}

void Product::setCategory(Category* a)
{
	if (a == nullptr) {
		cout << "The category parameter cannot be null!!\n";
		exit(1);
	}
	else
	{
		this->Category_ = a;
	}
}

Category* Product::getCategory()
{
	return this->Category_;
}



string Product::getDescription()
{
	return this->Description;
}



void Product::setDescription(string b)
{
	if (b != "") {
		this->Description = b;
	}
	else
	{
		cout << "Invalid input ron the description parameter\n";
	}
}

double Product::getPrice()
{
	return this->price;
}

double Product::getDiscount()
{
	return this->Discount;
}

int Product::getQuantity()
{
	return this->Quantity;
}


//implementing the methods of class Product
double Product::getEffectivePrice()
{

	if (this->type == amount) {
		return this->price - this->Discount;
	}
	else
	{
		return this->price - this->price * (this->Discount / 100);
	}
}

double Product::getTotalPrice()
{
	return  Product::getEffectivePrice() * this->Quantity;

}