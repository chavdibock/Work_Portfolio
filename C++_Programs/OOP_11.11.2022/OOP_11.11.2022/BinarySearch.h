#pragma once
#include <string>
using namespace std;
class BinarySerach
{
public:
	BinarySerach(string);
	string getS();
	void setS(string);
	int convertToInteger();


private:
	string s;
};