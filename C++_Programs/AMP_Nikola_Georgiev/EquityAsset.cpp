#include "EquityAsset.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include <vector>
#include <random>

EquityAsset::EquityAsset(string name, string symb, double prcPrc, double quant) : Asset(name, symb)
{
	setPrice(prcPrc);
	setCurefntPrice();
	setQuantity(quant);

}
double EquityAsset::getPrice()
{
	return this->purchasePrice;
}

void EquityAsset::setPrice(double price_)
{
	if (price_ == NULL || price_ <= 0) {
		cout << "Invalid price input" << endl;
	}
	else {
		this->purchasePrice = price_;
	}
}

double EquityAsset::assesRisk()
{
	cout << "To do//" << endl;
	return 0.0;
}

double EquityAsset::getQuantity()
{
	return this->quantity;
}

void EquityAsset::setQuantity(double quant)
{
	if (quant == NULL || quant <= 0.0) {
		cout << "Invalid quantity input" << endl;
	}
	else {
		this->quantity = quant;
	}
}

double EquityAsset::calcolateROI()
{

	return (getCurentPrice() - getPrice()) * getQuantity();

}

double EquityAsset::getCurentPrice()
{
	return this->curentPrice;

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


vector<struct MarketDataEq> EquityAsset::getPrevDataEq()
{
	string path = "resources/" + this->getSymbol() + ".csv";

	ifstream ins;

	ins.open(path);

	if (ins.fail()) {     // check if there was an error
		cout << "Error opening file ";

	}
	else
	{
		vector<MarketDataEq> dataSet;

		string mytxt;
		getline(ins, mytxt);
		while (!ins.eof()) {
			MarketDataEq data;
			getline(ins, mytxt);
			istringstream ss(mytxt);
			getline(ss, data.date, ',');
			getline(ss, data.open, ',');
			getline(ss, data.high, ',');
			getline(ss, data.low, ',');
			getline(ss, data.adjClose, ',');
			getline(ss, data.close, ',');
			getline(ss, data.volume, ',');

			dataSet.push_back(data);
		}

		return dataSet;

	}

	ins.close();

}


void EquityAsset::display()
{
	vector<MarketDataEq> prevData = this->getPrevDataEq();

	for (int i = 0; i < prevData.size(); i++)
	{
		cout << prevData[i].volume << endl;
	}
}

void EquityAsset::setCurefntPrice() // -+ 10% from the average of a .csv file for a particular asset
{
	vector<MarketDataEq> prevData = this->getPrevDataEq();


	// Clalculating the sum
	double sum = 0;

	for (int i = 0; i < prevData.size(); i++)
	{
		try {
			sum += stod(prevData[i].close);
		}
		catch (const invalid_argument& e) {
			cerr << "Invalid argument: " << e.what() << endl;
		}
		catch (const out_of_range& e) {
			cerr << "Out of range: " << e.what() << endl;
		}
	}

	double avg = sum / prevData.size();


	// random ogj for the percents
	random_device rdPer;
	mt19937 genPer(rdPer());


	// Define a distribution for the random numbers

	uniform_real_distribution<double> distribution(0, 0.10);
	double random_number = distribution(genPer);

	uniform_int_distribution<int> newSign(0, 1);
	int randomSign = newSign(genPer);

	// decide if to substract or add 10%
	if (randomSign == 0) {
		this->curentPrice = avg * (1.0 - random_number);
	}
	else {
		this->curentPrice = avg * (1.0 + random_number);
	}
}

