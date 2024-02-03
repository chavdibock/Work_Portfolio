#pragma once
#include <string>
#include <vector>
using namespace std;
class Item
{
public:
	Item(string, string);
	virtual  double getTotalPrice();
	string getTextKey();
	string getName();
	void setTextKey(string);
	void setName(string);
	vector<int> computeLPS(const string&);
	void KPM(const string& pattern);

protected:
	string TextKey, Name;
};
