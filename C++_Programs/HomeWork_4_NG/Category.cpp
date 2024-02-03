#include "Category.h"
#include <iostream>
#include <vector>
using namespace std;

Category::Category()	
{
	this->Name = "default";
	this->Parent = nullptr;
	this->Description = "def description";
	this->TextKey = "default-key";

}

vector<string> arr;

Category::Category(string name, string textKey, string Description, Category* a = nullptr)
{
	//using setters for the constructor
	setName(name);
	setDescription(Description);
	setTextKeys(textKey);
	setParent(a);
}
//Implementing Setters and Getters
string Category::getTextKeys()
{
	return this->TextKey;
}

string Category::getName()
{
	return this->Name;
}

string Category::getDescription()
{
	return this->Description;
}

string Category::getParent()
{
	if (this->Parent == nullptr) {
		cout << "Category " << this->getName() << " does not have parent.\n";
	}
	else {
		return this->Parent->Name;

	}

}

void Category::setParent(Category* per)
{

	if (per != nullptr) {
		this->Parent = per;
	}
	else {
		cout << "Category "<< this->getName() << " will not have parent\n";
	}
}

void Category::setTextKeys(string key)
{
	if (count(arr.begin(), arr.end(), key)) {
		cerr << "The key has already been used\n";
		exit(1);
	}
	else {
		this->TextKey = key;
		arr.push_back(key);
		cout << "success\n";

	}

}

void Category::setName(string name)
{
	if (name != "") {
		this->Name = name;
	}
	else {
		cout << "Name cannot be NULL!!!!\n";
		exit(1);
	}
}

void Category::setDescription(string desc)
{

	if (desc != "") {
		this->Description = desc;
	}
	else {
		cout << "Description cannot be NULL!!!\n";
		exit(1);
	}

}
