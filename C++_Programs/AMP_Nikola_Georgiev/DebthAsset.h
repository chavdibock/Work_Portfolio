#pragma once
#include "Asset.h"
enum couponType {
	year, halfYear, quaterYear, thirdYear, month
};

class DebthAsset : public Asset
{
public:
	DebthAsset(string,string,couponType, double, double);
	couponType getCouponType();
	void setCouponType(couponType);
	void setInitialAmount(double);
	double getInitialAmount();
	double getInterestRate();
	void setInterestRate(double);
	vector<struct MarketData> getPrevDataDp();



protected:
	couponType coupon;
	double initialAmount;
	double interestRate;

};