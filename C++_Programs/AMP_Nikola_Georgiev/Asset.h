#pragma once
#include <string>
#include <vector>
using namespace std;
class Asset
{
public:
	//constructor
	Asset(string, string);
	
	//getters
	string getName();
	string getSymbol();
	//seters
	void setSymbol(string);
	void setName(string);
	virtual double assesRisk();
	static int divide(vector<Asset*>& arr, int, int);
	static void quicksort(vector<Asset*>& arr, int, int);

protected:
	string name, symbol;
	
};
