#pragma once
#include "EquityAsset.h"
class CryptoCurency : public EquityAsset
{
public:
	CryptoCurency(string, string, double, double, string);
	string getblockChain();
	void setblockChain(string);
	double assesRisk();


private:
	string blockChain;
};