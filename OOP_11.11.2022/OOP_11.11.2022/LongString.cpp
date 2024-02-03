#include "LongString.h"
#include <string>
#include <iostream>
LongString::LongString(string s)
{
	value = s;

}

string LongString::getValue()
{
	return value;
}

void LongString::setValue(string s)
{
	if (s.length() < 0) {
		cout << "Erorr";
	}
	else
	{
		value = s;
	}
}

int LongString::length()
{
	return value.length();
}

char LongString::get(int p)
{
	if (p >= 0 && p <= value.length()) {
		return value[p];
	}
	else {
		cout << "error";
	}
	
}

void LongString::addString(const LongString& s)
{
	value += s.value;
	cout << value;
}
