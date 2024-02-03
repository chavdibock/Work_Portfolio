#include <iostream>
#include "Book.h"
#include <string>

using namespace std;

Book::Book()
{
	name = "NIkola's book";
	author = "nikola";
	pages = 100;


}

Book::Book(string n, string a, int p)
{
	
	setName(n);
	setAuthor(a);
	setPages(p);
}

string Book::getName()
{
	return name;
}

void Book::setName(string n)
{
	if (n.length() != 0) {
		this -> name = n;
	}
	else {
		cout << "invalid input";
	}
}

string Book::getAuthor()
{
	return author;
}

void Book::setAuthor(string a)
{
	if (a.length() != 0) {
		this-> author = a;
	}
	else {
		cout<< "invalid input";
	}
}

int Book::getPages()
{
	return pages;
}

void Book::setPages(int p)
{
	if (p > 0) {
		this-> pages = p;
	}
	else {
		cout << "invalid input";
	}
}

void Book::type() const
{
	cout << "this is a virtual void" << endl;
}

bool Book::operator==(const Book& s) const
{
	if (name == s.name && author == s.author) {
		return true;
	}
	else {
		return false;
	}
}
