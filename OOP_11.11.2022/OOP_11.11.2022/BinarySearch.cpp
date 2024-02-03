#include<iostream>
#include<string>
#include <cmath>
#include "BinarySearch.h"
using namespace std;

BinarySerach::BinarySerach(string str)
{
	if (str.length() == 5) {
		s = str;
	}
	else {

		cout << "error";
	}
}

string BinarySerach::getS()
{
	return s;
}

void BinarySerach::setS(string str)
{
	if (str.length() == 5) {
		s = str;
	}
	else {

		cout << "error";
	}
}

int BinarySerach::convertToInteger()
{
	int a = 0;
	int power = 0;
	bool fls = false;

	for (int i = s.length()-1; i >=0; i--) 
	{
		
		switch (s[i])
		{
		case '1':
			a += pow(2, power);
			break;
		case '0':
			a += 0;
			break;
		default:
			fls = true;

		}
		power++;
	}



	if (!fls) {
		return a;
	}
	else {
		return a = -1;
	}

	
}
