#include "DebthAsset.h"
#include <iostream>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include <vector>
#include <random>
using namespace std;

DebthAsset::DebthAsset(string name, string symb_, couponType coupType, double initialAmount, double intr) : Asset(name, symb_)
{
	setCouponType(coupType);
	setInitialAmount(initialAmount);
	setInterestRate(intr);

}

couponType DebthAsset::getCouponType()
{
	return this->coupon;
}

void DebthAsset::setCouponType(couponType cpType)
{

	if (cpType == year || cpType == halfYear || cpType == quaterYear ||
		cpType == thirdYear || cpType == month)
	{
		this->coupon = cpType;

	}
	else {
		cout << "Invalid input for the coupon type" << endl;
	}

}

void DebthAsset::setInitialAmount(double intAmount)
{
	if (intAmount <= 0) {
		cout << "Invalid Input" << endl;
	}
	else {
		this->initialAmount = intAmount;
	}
}

double DebthAsset::getInitialAmount()
{
	return this->initialAmount;
}

double DebthAsset::getInterestRate()
{
	return this->interestRate;
}

void DebthAsset::setInterestRate(double intR)
{
	if (intR <= 0) {
		cout << "Invalid inout for the interest rate!!!" << endl;
	}
	else {

		this->interestRate = intR;
	}
}

struct MarketData {
	string date;
	string name;
	string rating;
};



vector<struct MarketData> DebthAsset::getPrevDataDp()
{
	
	string path = "resources/" + this->getSymbol() + ".csv";

	ifstream ins;

	ins.open(path);


	if (ins.fail()) {     // check if there was an error
		cout << "Error opening file";
	}
	else
	{
		vector<MarketData> dataSet;

		string mytxt;
		getline(ins, mytxt);
		while (!ins.eof()) {
			MarketData data;
			getline(ins, mytxt);
			istringstream ss(mytxt);
			getline(ss, data.date, ',');
			getline(ss, data.name, ',');
			getline(ss, data.rating, ',');

			dataSet.push_back(data);
		}

		return dataSet;

	}
	


	ins.close();


}


