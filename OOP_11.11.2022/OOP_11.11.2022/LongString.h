#pragma once
#include <string>
using namespace std;
class LongString
{
public:
	LongString(string);
	string getValue();
	void setValue(string);
	int length();
	char get(int);
	void addString(const LongString& s);

private:
	string value;
};
