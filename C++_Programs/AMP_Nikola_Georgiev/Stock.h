#pragma once
#include "EquityAsset.h"
class Stock : public EquityAsset
{
public:
	Stock(string, string, double, double, int);
	int getShareOutstanding();
	void setShareOutstanding(int);
	double assesRisk();
private:
	int sharesOutstanding;
};
