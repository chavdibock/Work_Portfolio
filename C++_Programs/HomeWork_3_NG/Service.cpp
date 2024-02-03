#include "Service.h"
#include <string>
#include <iostream>

using namespace std;

Service::Service(string name, string tKey, string decrp, double prc, double dsc, Category* ctgr, int quant, DiscountType dscType, double dur, double rate, double rtDsc, RateDiscountType rtDscType)
	: Product(name, tKey, decrp, prc, dsc, ctgr, quant, dscType)
{
	//using setter for the constructor
	setDuration(dur);
	setRate(rate);
	setDiscountRate(rtDsc);
	setRateDiscountType(rtDscType);
}
//Implementing setters and getters
double Service::getDuration()
{
	return this->Duration;
}

double Service::getRate()
{
	return this->Rate;
}

double Service::getDiscount()
{
	return this->RateDiscount;
}

RateDiscountType Service::getDiscountType()
{
	return this->rateDiscountType_;
}

void Service::setDuration(double dur)
{
	if (dur < 0) {
		cout << "Invalid input of the duration parameter for service " << getName() << "\n";
		exit(1);
	}
	else
	{
		this->Duration=dur;
	}
}

void Service::setRate(double rt)
{
	if (rt < 0) {
		cout << "Invalid input of the rate parameter for service " << getName() << "\n";
		exit(1);
	}
	else
	{
		this->Rate = rt;
	}
}

void Service::setDiscountRate(double rtdsc)
{
	if (rtdsc < 0) {
		cout << "Invalid input of the discountRate parameter for service " << getName() << "\n";
		exit(1);
	}
	else
	{
		this->RateDiscount = rtdsc;
	}
}

void Service::setRateDiscountType(RateDiscountType rtDiscType)
{
	if (rtDiscType == percentage_ || rtDiscType == amount_) {

		this->rateDiscountType_ = rtDiscType;
	}
	else {
		cout << "Invalid discount type!!!\n";
		exit(1);

	}
}

//Implementing the methods of class Service
double Service::getEffectivePrice()
{
	if (this->rateDiscountType_ == amount_)
	{
		return this->Rate - this->RateDiscount;
	}
	else {

		return this->Rate - (this->Rate * (this->RateDiscount/100));
	}


}

double Service::getTotalPrice()
{
	 
	return  Product::getTotalPrice() + (Service::getEffectivePrice() *this->Duration);
}
