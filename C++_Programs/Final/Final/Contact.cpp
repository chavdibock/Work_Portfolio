#include <iostream>
#include <string>
#include "Contact.h"
using namespace std;

Contact::Contact()
{
	name = "Nikola";
	address = "AUBG";

}

Contact::Contact(string n, string a)
{

	name = n;
	address = a;
}

Contact::Contact(const Contact& p)
{
	address = p.address;
	name = p.name;
}


