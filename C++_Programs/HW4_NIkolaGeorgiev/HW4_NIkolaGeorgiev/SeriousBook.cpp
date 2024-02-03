#include"SeriousBook.h"
#include <iostream>
#include <string>

SeriousBook::SeriousBook() :Book()
{
	this->genre = "serius";
}

SeriousBook::SeriousBook(string n, string a, int p, string g) : Book(n,a,p)
{
	setGenre(g);
}

string SeriousBook::getGenre()
{
	return genre;
}

void SeriousBook::setGenre(string g)
{
	if (g.length() != 0) {
		this->genre = g;
	}
	else {
		cout << "invalid input";
	}
}

void SeriousBook::type() const
{
	cout << "Serious book, genre: " << genre << endl;
}
