#pragma once
#include "Asset.h"

class EquityAsset : public Asset
{
public:
	EquityAsset(string, string, double, double);

	double getPrice();
	void setPrice(double);
	
	double getQuantity();
	void setQuantity(double);
	double calcolateROI();
	double getCurentPrice();
	void setCurefntPrice();
	vector<struct MarketDataEq> getPrevDataEq();
	void display();
	double assesRisk();
private:
	string name, Symbol;
	double purchasePrice, quantity, curentPrice;


};