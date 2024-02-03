#include "Rectangle.h"
#include <iostream>
using namespace std;
Rectangle::Rectangle()
{
	height = 1;
	width = 10;
}

Rectangle::Rectangle(int a, int b)
{ 
	setHeight(a);
	setwidht(b);

}

int Rectangle::getHeight()
{
	return height;
}

int Rectangle::getWidth()
{
	return width;
}

void Rectangle::setHeight(int a)
{
	if (a>=0){
		height = a;
	}
	else {
		cout << "It can't be negative number";
	}
}

void Rectangle::setwidht(int b)
{
	if (b>=0)
	{
		width = b;
	}
	else {
		cout << "It can't be negative number";
	}
}

int Rectangle::getAera()
{
	return height*width;
}
