

#include <iostream>
#include "Asset.h"
#include "EquityAsset.h"
#include "DebthAsset.h"
#include "BankDeposit.h"
#include "Stock.h"
#include "CryptoCurency.h"
#include "Bond.h"
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;





couponType stringToEnum(const std::string& str) {
	if (str == "year") {
		return year;
	}
	else if (str == "halfYear") {
		return halfYear;
	}
	else if (str == "month") {
		return month;
	}
	else if (str == "quaterYear") {
		return quaterYear;
	}
	else if (str == "thirdYear") {
		return thirdYear;
	}
	else {
		cerr << "Invalid input";
	}
}



int main()
{
	vector<Asset*> dataAsset;

	string pathBankDeposit = "resources/inputData/BankDeposit.csv";
	string pathBond = "resources/inputData/Bond.csv";
	string pathStock = "resources/inputData/Stock.csv";
	string pathCryptoCurency = "resources/inputData/CryptoCurency.csv";


	ifstream ins;
	// Geting the data for the bank deposits
	ins.open(pathBankDeposit);
	if (ins.fail()) { // check if there was an error
		cout << "Error file";
	}
	else { // Looking trough the file 
		string mytxt;
		getline(ins, mytxt);
		while (!ins.eof()) {
			string name, symb, couptype, openingDate, initilaAmount, interestRate;
			getline(ins, mytxt);
			istringstream ss(mytxt);
			getline(ss, name, ',');
			getline(ss, symb, ',');
			getline(ss, couptype, ',');
			getline(ss, initilaAmount, ',');
			getline(ss, interestRate, ',');
			getline(ss, openingDate, ',');

			double intAmount, intRate;
			couponType cpType = stringToEnum(couptype);

			try {
				intAmount = stod(initilaAmount);
				intRate = stod(interestRate);
			}
			catch (const invalid_argument& e) {
				cerr << "Invalid argument: " << e.what() << endl;
			}
			catch (const out_of_range& e) {
				cerr << "Out of range: " << e.what() << endl;
			}
		

			//BankDeposit bankDep(name, symb, cpType, intAmount, intRate, openingDate);
			//cout << "Succecfull creation of " << bankDep.getSymbol() << endl;

			dataAsset.emplace_back(new BankDeposit(name, symb, cpType, intAmount, intRate, openingDate));
		}
	}
	ins.close();

	//Geting the data for the bonds
	ins.open(pathBond);

	if (ins.fail()) { // check if there was an error
		cout << "Error file";
	}
	else {
		string mytxt;
		getline(ins, mytxt);
		while (!ins.eof())
		{
			string name, symb, couptype, exprDate, initilaAmount, interestRate;
			getline(ins, mytxt);
			istringstream ss(mytxt);
			getline(ss, name, ',');
			getline(ss, symb, ',');
			getline(ss, couptype, ',');
			getline(ss, initilaAmount, ',');
			getline(ss, interestRate, ',');
			getline(ss, exprDate, ',');

			double intAmount, intRate;
			couponType cpType = stringToEnum(couptype);

			try {
				intAmount = stod(initilaAmount);
				intRate = stod(interestRate);
			}
			catch (const invalid_argument& e) {
				cerr << "Invalid argument: " << e.what() << endl;
			}
			catch (const out_of_range& e) {
				cerr << "Out of range: " << e.what() << endl;
			}


			//BankDeposit bankDep(name, symb, cpType, intAmount, intRate, openingDate);
			//cout << "Succecfull creation of " << bankDep.getSymbol() << endl;

			dataAsset.emplace_back(new Bond(name, symb, cpType, intAmount, intRate, exprDate));
		}
	}
	ins.close();


	// Geting the data for the Stocks
	ins.open(pathStock);
	if (ins.fail()) { // check if there was an error
		cout << "Error file";
	}
	else { // Looking trough the file 
		string mytxt;
		getline(ins, mytxt);
		while (!ins.eof()) {
			string name, symb, prc, quant, oustShares;
			getline(ins, mytxt);
			istringstream ss(mytxt);
			getline(ss, name, ',');
			getline(ss, symb, ',');
			getline(ss, prc, ',');
			getline(ss, quant, ',');
			getline(ss, oustShares, ',');

			double price, quantity, outShrs;

			try {
				price = stod(prc);
				quantity = stod(quant);
				outShrs = stod(oustShares);

			}
			catch (const invalid_argument& e) {
				cerr << "Invalid argument: " << e.what() << endl;
			}
			catch (const out_of_range& e) {
				cerr << "Out of range: " << e.what() << endl;
			}


			//BankDeposit bankDep(name, symb, cpType, intAmount, intRate, openingDate);
			//cout << "Succecfull creation of " << bankDep.getSymbol() << endl;

			dataAsset.emplace_back(new Stock(name, symb, price, quantity, outShrs));
		}
	}
	ins.close();

	// Geting the info for Crypto Curency
	ins.open(pathCryptoCurency);
	if (ins.fail()) { // check if there was an error
		cout << "Error file";
	}
	else { // Looking trough the file 
		string mytxt;
		getline(ins, mytxt);
		while (!ins.eof()) {
			string name, symb, prc, quant, blcChain;
			getline(ins, mytxt);
			istringstream ss(mytxt);
			getline(ss, name, ',');
			getline(ss, symb, ',');
			getline(ss, prc, ',');
			getline(ss, quant, ',');
			getline(ss, blcChain, ',');

			double price, quantity, outShrs;

			try {
				price = stod(prc);
				quantity = stod(quant);

			}
			catch (const invalid_argument& e) {
				cerr << "Invalid argument: " << e.what() << endl;
			}
			catch (const out_of_range& e) {
				cerr << "Out of range: " << e.what() << endl;
			}


			//BankDeposit bankDep(name, symb, cpType, intAmount, intRate, openingDate);
			//cout << "Succecfull creation of " << bankDep.getSymbol() << endl;

			dataAsset.emplace_back(new CryptoCurency(name, symb, price, quantity, blcChain));
		}
	}
	ins.close();



	Asset::quicksort(dataAsset, 0, dataAsset.size()-1);

	for (int i = 0; i < dataAsset.size(); i++) {
		cout << dataAsset[i]->getName() << " -> " << dataAsset[i]->assesRisk() << endl;
	}

	return 0;

}