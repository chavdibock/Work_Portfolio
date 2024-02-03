#pragma once
#include<string>
#include "Item.h"
#include "Category.h"
using namespace std;

enum DiscountType
{
	amount, percentage
};

class Product : public Item
{
public:

	Product(string,string,string,double,double,Category*,int,enum DiscountType);
	string getDescription();

	void setDescription(string);
	double getPrice();
	double getDiscount();
	int getQuantity();
	void setQuantity(int);
	void setPrice(double);
	void setDiscount(double);
	DiscountType getDiscountType();
	void setDiscountType(DiscountType);
	void setCategory(Category*);
	Category* getCategory();
	virtual double getEffectivePrice();
	double getTotalPrice();


protected:
	string TextKey, Name, Description;
	double price, Discount;
	Category* Category_;
	int Quantity;
	DiscountType type;

};
