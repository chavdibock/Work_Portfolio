#include "Item.h"
#include  <iostream>
#include <vector>
using namespace std;


vector<string> arrpr;


Item::Item(string name, string key)
{
	setName(name);
	setTextKey(key);
}

double Item::getTotalPrice()
{
    return 0.0;
}

string Item::getTextKey()
{
	return this->TextKey;
}

string Item::getName()
{
	return this->Name;
}

void Item::setTextKey(string key)
{
	if (count(arrpr.begin(), arrpr.end(), key)) {
		cerr << "The key for product " << getName() << "has already been used\n";
		exit(1);
	}
	else {
		this->TextKey = key;
		arrpr.push_back(key);
		cout << "success\n";

	}
}

void Item::setName(string a)
{
	if (a != "") {
		this->Name = a;
	}
	else
	{
		cout << "Invalid input ron the name parameter\n";
	}
}

vector<int> Item::computeLPS(const string& pattern)
{
	int n = pattern.size();
	vector<int> lps(n, 0);

	int len = 0;
	int i = 1;

	while (i < n) {
		if (pattern[i] == pattern[len]) {
			len++;
			lps[i] = len;
			i++;
		}
		else {
			if (len != 0) {
				len = lps[len - 1];
			}
			else {
				lps[i] = 0;
				i++;
			}
		}
	}

	return lps;
}

void Item::KPM(const string& pattern)
{
	int n = this->getName().size();
	int m = pattern.size();

	vector<int> lps = computeLPS(pattern);
	
	int i = 0;  // Index for text[]
	int j = 0;  // Index for pattern[]

	while (i < n) {
		if (pattern[j] == this->getName()[i]) {
			i++;
			j++;
		}

		if (j == m) {
			cout << "Pattern found for " << this->getName() << endl;
			j = lps[j - 1];
		}
		else if (i < n && pattern[j] != this->getName()[i]) {
			if (j != 0) {
				j = lps[j - 1];
			}
			else {
				i++;
			}
		}
	}
}
