#include <iostream>
#include <string>
#include "DiaryProduct.h"
using namespace std;

DiaryProduct::DiaryProduct()
{
	name = "AUBG";
	price = 10.3;
}

string DiaryProduct::getName()
{
	return name;
}

double DiaryProduct::getPrice()
{
	return price;
}
