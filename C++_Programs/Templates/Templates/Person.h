#pragma once
#include <iostream>
#include <string>
using namespace std;
class Person
{
public:
	Person();
	Person(string, int);
	void setAge(int);
	void setName(string);
	int getAge();
	string getName();
	Person(const Person& p);
	~Person();


private:
	int age;
	string name;
};

