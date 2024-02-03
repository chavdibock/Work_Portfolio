#include "Person.h"
#include <iostream>
#include <string>

Person::Person()
{
	age = 10;
	name = "Veri";

}

Person::Person(string n, int a)
{
	setAge(a);
	setName(n);
}

void Person::setAge(int a)
{
	if (a > 0) {
		age = a;
	}
	else {
		cout << "invalid input" << endl;
		age = 10;
	}
}

void Person::setName(string n)
{
	if (n.length() != 0) {
		name = n;
	}
	else {
		cout << "invalid input" << endl;
		name = "Veri";
	}
}

int Person::getAge()
{
	return age;
}

string Person::getName()
{
	return name;
}

Person::Person(const Person& p)
{
	age = p.age;
	name = p.name;
}

Person::~Person()
{
}
