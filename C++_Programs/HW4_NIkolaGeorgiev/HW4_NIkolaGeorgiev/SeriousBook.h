#pragma once
#include "Book.h"
#include <iostream>
#include <string>

using namespace std;

class SeriousBook : public Book
{
public:
	SeriousBook();
	SeriousBook(string, string , int , string);
	string getGenre();
	void setGenre(string);
	void type() const;
private:
	string genre;
};
