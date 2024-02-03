#include "CryptoCurency.h"
#include <iostream>
CryptoCurency::CryptoCurency(string name, string symb, double prc, double quant, string blcChain) : EquityAsset(name, symb, prc, quant)
{
	setblockChain(blcChain);
	
}

string CryptoCurency::getblockChain()
{
	return string();
}

void CryptoCurency::setblockChain(string name)
{
	if (name != "") {
		this->blockChain = name;
	}
	else
	{
		cout << "Invalid input in for the name" << endl;
	}

}

struct MarketDataEq {
	string date;
	string open;
	string high;
	string low;
	string close;
	string adjClose;
	string volume;
};
double CryptoCurency::assesRisk()
{


	vector<MarketDataEq> prevData = this->getPrevDataEq();


	// Clalculating the sum
	double sumHigh = 0;
	double sumLow = 0;

	for (int i = 0; i < prevData.size(); i++)
	{
		try {
			sumHigh += stod(prevData[i].high);
			sumLow += stod(prevData[i].low);
		}
		catch (const invalid_argument& e) {
			cerr << "Invalid argument: " << e.what() << std::endl;
		}
		catch (const out_of_range& e) {
			cerr << "Out of range: " << e.what() << std::endl;
		}
	}


	return abs(sin((sumHigh - sumLow) * abs(cos(sqrt(getCurentPrice()))))) * 100;

}
