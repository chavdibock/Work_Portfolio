#pragma once
#include "DebthAsset.h"
class BankDeposit : public DebthAsset
{
public:
	BankDeposit(string, string, couponType, double, double, string);
	string getOpeningDate();
	void setOpeningDate(string);
	double curentReturn();
	double assesRisk();
private:
	string openingDate;
	
};
