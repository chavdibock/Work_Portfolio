#include "Circle.h"
#include <iostream>
using namespace std;
Circle::Circle(double r)
{
	radius = r;
}

double Circle::getRadius()
{
	return radius;
}

void Circle::setRadius(double r)
{
	if (r >=0) {
		radius = r;
	}
	else {
		cout << "Error!!";
	}
}

double Circle::getArea()
{
	return radius*radius*3.14 ;
}


double Circle::getParameter()
{
	return radius*2*3.14;
}
