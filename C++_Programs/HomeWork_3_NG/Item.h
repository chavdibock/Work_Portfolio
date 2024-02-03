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
	static int divide(vector<Item*> &arr,int, int);
	static void quicksort(vector<Item*> &arr, int, int);
protected:
	string TextKey, Name;
};