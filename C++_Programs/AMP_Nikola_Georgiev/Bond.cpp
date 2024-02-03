#include "Bond.h"
#include <iostream>
#include <chrono>
#include <sstream>
#include <iomanip>


Bond::Bond(string name, string symb_, couponType coupType, double initialAmount, double interest, string exprDate) : DebthAsset(name, symb_, coupType, initialAmount, interest)
{
	setExpirationDate(exprDate);
}

string Bond::getExpirationDate()
{
	return this->expirationDate;
}

void Bond::setExpirationDate(string expDate)
{
	if (expDate != "") {
		this->expirationDate = expDate;
	}
	else
	{
		cout << "Invalid input dor expiration date";
	}
}

double Bond::remainingReturn()
{
	int devideBY = 0;
	switch (getCouponType())
	{
	case year:
		devideBY = 12;
		break;

	case halfYear:
		devideBY = 6;
		break;

	case quaterYear:
		devideBY = 4;
		break;

	case thirdYear:
		devideBY = 3;
		break;

	case month:
		devideBY = 1;
		break;

	}

	istringstream iss1(getExpirationDate());
	tm tm1{};
	iss1 >> get_time(&tm1, "%Y-%m-%d");

	// Create time points for the two dates
	auto date1 = chrono::system_clock::from_time_t(mktime(&tm1));
	auto currentDate = chrono::system_clock::now();

	// Calculate the duration between the two dates in days
	auto duration = chrono::duration_cast<chrono::hours>(date1 - currentDate);
	auto days = duration.count() / 24;  // Convert hours to days

	// Assuming an average of 30.44 days in a month
	auto numMonths = static_cast<int>(days / (30.44 * devideBY));


	double amount = 0;

	for (int i = 0; i < numMonths; i++)
	{
		amount +=  getInitialAmount() * getInterestRate();
	}

	return amount;


}

struct MarketData {
	string date;
	string name;
	string rating;
};


double Bond::assesRisk()
{
	vector<MarketData> prevData = this->getPrevDataDp();

	double sumRating = 0;


	for (int i = 0; i < prevData.size(); i++)
	{
		try {
			sumRating += stod(prevData[i].rating);
		}
		catch (const invalid_argument& e) {
			cerr << "Invalid argument: " << e.what() << std::endl;
		}
		catch (const out_of_range& e) {
			cerr << "Out of range: " << e.what() << std::endl;
		}
	}

	double avgRating = sumRating / prevData.size();
	return abs(sin(sqrt(avgRating) * cos(getInterestRate() * getInitialAmount()))) * 100;
	
}
