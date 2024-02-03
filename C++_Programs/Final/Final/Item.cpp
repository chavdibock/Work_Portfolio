#include <iostream>
#include "Item.h"
#include <string>
using namespace std;

bool Item::operator<(const Item& itm) const
{
	if (*price < *itm.price) {
		return true;
	}
	else {
		return false;
	}
}
