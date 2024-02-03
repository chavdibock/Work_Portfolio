#pragma once
#include "Product.h"
#include <string>

enum RateDiscountType
{
	amount_, percentage_
};

class Service : public Product
{
public:
	//Constructor
	Service(string, string, string, double, double, Category*, int, enum DiscountType, double, double, double, RateDiscountType);
	double getDuration();
	double getRate();
	double getDiscount();
	RateDiscountType getDiscountType();
	void setDuration(double);
	void setRate(double);
	void setDiscountRate(double);
	void setRateDiscountType(RateDiscountType);
	double getEffectivePrice();
	double getTotalPrice();


private:
	double Duration, Rate, RateDiscount;
	RateDiscountType rateDiscountType_;

};