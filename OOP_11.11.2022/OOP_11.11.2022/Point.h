#pragma once
class Point
{
public:
	Point();
	Point(double, double);
	double getX();
	double gerY();
	void setX(double);
	void setY(double);
	double calcDistance(const Point&);

private:
	double x;
	double y;
};
