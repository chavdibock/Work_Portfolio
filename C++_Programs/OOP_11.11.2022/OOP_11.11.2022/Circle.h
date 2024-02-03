#pragma once
class Circle
{
public:
	Circle(double);
	double getRadius();
	void setRadius(double);
	double getArea();
	double getParameter();
private:

	double radius;
};