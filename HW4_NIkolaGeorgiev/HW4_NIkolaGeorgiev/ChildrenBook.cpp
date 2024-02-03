
#include "ChildrenBook.h"
#include <iostream>
#include <string>


ChildrenBook::ChildrenBook():Book()
{
	this ->ageAppropriate = 12;
}

ChildrenBook::ChildrenBook(string name, string author, int page, int age) : Book(name,author,page)
{
	setAgeAppropriate(age);
}


int ChildrenBook::getAgeAppropriate()
{
	return ageAppropriate;
}

void ChildrenBook::setAgeAppropriate(int a)
{
	if (a > 0)
	{
		ageAppropriate = a;
	}
	else {
		ageAppropriate = 12;
	}
}

void ChildrenBook::type() const
{
	cout << "Children book for age of  " << ageAppropriate << " and older" << endl;
}

istream& operator >>(istream& in, ChildrenBook& c)
{
	string name, author;
	int page, age;
	cout << "Enter the name of the book, the author, the pages and the age" << endl;
	getline(in, name);
	getline(in, author);
	in >> page >> age;
	c.setName(name);
	c.setAuthor(author);
	c.setPages(page);
	c.setAgeAppropriate(age);

	return in;
}