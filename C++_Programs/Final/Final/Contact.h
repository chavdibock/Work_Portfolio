#pragma once
#include <iostream>
#include <string>
using namespace std;
class Contact
{
public:
	Contact();
	Contact(string, string);
	Contact(const Contact& p);



private:
	string name, address;	
};
