#pragma once
#include "Book.h"
#include <iostream>
#include <string>
class ChildrenBook : public Book
{
public:
	ChildrenBook();
	ChildrenBook(string, string, int, int);
	int getAgeAppropriate();
	void setAgeAppropriate(int);
	void type() const;
	friend istream& operator>>(istream&, ChildrenBook&);
private:
	int ageAppropriate;
};
