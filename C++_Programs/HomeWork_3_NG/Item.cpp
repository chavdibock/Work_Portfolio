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

int Item::divide(vector<Item*> &arr, int low, int high)
{
	double pivot = arr[high]->getTotalPrice();
	int i = (low - 1);
	for (int j = low; j <= high - 1; j++) {
		// If current element is smaller than the pivot
		if (arr[j]->getTotalPrice() < pivot) {
			// Increment index of smaller element
			i++;
			std::swap(arr[i], arr[j]);
		}
	}
	Item* temp = reinterpret_cast<Item*>(&arr[i + 1]);
	swap(arr[i + 1], arr[high]);
	return(i + 1);

}

void Item::quicksort(vector<Item*> &arr, int low, int high)
{
	if (low < high) {
		int pivot = divide(arr, low, high);
		quicksort(arr, low, pivot - 1);
		quicksort(arr, pivot + 1, high);
	}
}
