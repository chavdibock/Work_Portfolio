#pragma once
#include "DebthAsset.h"

class Bond : public DebthAsset
{
public:
	Bond(string, string, couponType, double, double, string);
	string getExpirationDate();
	void setExpirationDate(string);
	double remainingReturn();
	double assesRisk();
private:
	string expirationDate;
};
