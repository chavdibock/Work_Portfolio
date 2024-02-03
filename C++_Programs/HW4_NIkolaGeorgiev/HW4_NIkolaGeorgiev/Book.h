#pragma once
#include <string>
using namespace std;
class Book
{
public:
	Book();
	Book(string ,string, int);

	string getName();
	void setName(string);

	string getAuthor();
	void setAuthor(string);

	int getPages();
	void setPages(int);

	virtual void type() const;
	
	bool operator==(const Book &) const;


private:
	string author, name;
	int pages;

};
