#include "Stock.h"
#include <iostream>

Stock::Stock(string name, string symb, double prc, double quant, int oustShares) : EquityAsset(name,symb,prc,quant)
{
	setShareOutstanding(oustShares);
}

int Stock::getShareOutstanding()
{
	return this->sharesOutstanding;
}

void Stock::setShareOutstanding(int shares)
{
	if (shares == NULL || shares <= 0) {
		cout << "Invalid input for outstanding shares" << endl;
	}
	else
	{
		this->sharesOutstanding = shares;
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
double Stock::assesRisk()
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

	double avgHigh = sumHigh / prevData.size();
	double avgLow = sumLow / prevData.size();

	double pred = 0;

	return sqrt(abs(sin((avgHigh - avgLow) * abs(cos(getShareOutstanding()/getCurentPrice())))))  * 100;
}
