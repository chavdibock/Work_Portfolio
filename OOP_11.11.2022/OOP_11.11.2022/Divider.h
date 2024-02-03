#pragma once
class Divider
{
public:
	Divider(double, double);
	void setNumerator(double);
	void setDenumerator(double);
	double getNumerator();
	double getDenumerator();
	double result(double, double);
	

private:
	double numerator, denumerator;
};


