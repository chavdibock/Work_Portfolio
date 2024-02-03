#pragma once
#include <string>
using namespace std;

class Category
{
public:
	Category();
	Category(string, string, string, Category*);
	string getTextKeys();
	string getName();
	string getDescription();
	string getParent();
	void setParent(Category*);
	void setTextKeys(string);
	void setName(string);
	void setDescription(string);
private:
	string TextKey, Name, Description;
	Category* Parent;


};
