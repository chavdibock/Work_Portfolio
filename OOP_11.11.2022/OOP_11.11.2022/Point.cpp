#include "Point.h"
#include <iostream>
#include <cmath>
using namespace std;

Point::Point()
{
	x = 0;
	y = 0;

}

Point::Point(double a, double b)
{
	if (a>=0 && b>= 0) {
		x = a;
		y = b;
	}
	else {
		cout << "Error";
	}
	
}

double Point::getX()
{
	return x;
}

double Point::gerY()
{
	return y;
}

void Point::setX(double a)
{
	if (a < 0) {
		cout << "error";
	}
	else {
		x = a;
	}


}

void Point::setY(double b)
{
	if (b < 0) {
		cout << "error";
	}
	else {
		y = b;
	}
}

double Point::calcDistance(const Point& p)
{
	return sqrt( pow(p.x - x,2) + pow(p.y - y,2)) ;
}
