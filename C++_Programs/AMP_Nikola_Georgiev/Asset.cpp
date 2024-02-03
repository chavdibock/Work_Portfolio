#include "Asset.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include <vector>

using namespace std;
vector<string> arr;

Asset::Asset(string a, string b)
{
	setName(a);
	setSymbol(b);
}

string Asset::getName()
{
	return this->name;
}

string Asset::getSymbol()
{
	return this->symbol;
}

void Asset::setSymbol(string s)
{
	if (s != "" && count(arr.begin(), arr.end(), s) == 0) {
		this->symbol = s;
		arr.push_back(s);
	}
	else
	{
		cerr << "Invalid Symbol" << endl;

	}
}

void Asset::setName(string n)
{
	if (n != "") {
		this->name = n;
	}
	else
	{
		cout << "Invalid input in for the name" << endl;
	}
}





double Asset::assesRisk()
{
	return 0.0;
}

int Asset::divide(vector<Asset*>& arr, int low, int high)
{
	double pivot = arr[high]->assesRisk();
	int i = (low - 1);
	for (int j = low; j <= high - 1; j++) {
		// If current element is smaller than the pivot
		if (arr[j]->assesRisk()<= pivot) {
			// Increment index of smaller element
			i++;
			std::swap(arr[i], arr[j]);
		}
	}
	Asset* temp = reinterpret_cast<Asset*>(&arr[i + 1]);
	swap(arr[i + 1], arr[high]);
	return(i + 1);
}

void Asset::quicksort(vector<Asset*>& arr, int low, int high)
{
	if (low < high) {
		int pivot = divide(arr, low, high);
		quicksort(arr, low, pivot - 1);
		quicksort(arr, pivot + 1, high);
	}
}
