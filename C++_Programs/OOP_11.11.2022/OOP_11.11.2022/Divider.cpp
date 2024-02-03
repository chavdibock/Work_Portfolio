#include"Divider.h"

Divider::Divider(double n, double m)
{
	numerator = n;
	denumerator = m != 0 ? m : 1;
	setDenumerator(m);

}

void Divider::setNumerator(double  n)
{
	numerator = n;
}

void Divider::setDenumerator(double d)
{
	denumerator = d;
}

double Divider::getNumerator()
{
	return numerator;
}

double Divider::getDenumerator()
{
	return denumerator;
}

double Divider::result(double n, double m)
{
	return n/m;
}
