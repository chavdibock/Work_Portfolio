#pragma once
#include <iostream>
#include <string>
#include "Product.h"
using namespace std;

class DiaryProduct : public Product
{
public:
	DiaryProduct();
	string getName();
	double getPrice();

private:
	string name;
	double price;
};

