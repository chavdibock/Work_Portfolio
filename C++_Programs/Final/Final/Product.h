#pragma once
#include <iostream>
#include <string>
using namespace std;
class Product
{
public:
	virtual string getName() = 0;
	virtual double getPrice() = 0;

private:

};

