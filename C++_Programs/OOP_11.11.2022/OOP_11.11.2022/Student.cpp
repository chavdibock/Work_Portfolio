#include<iostream>
#include<string>
#include "Student.h"


Student::Student()
{
	name = "John";
	quiz = 0;
	exam = 0;
}

Student::Student(string n, double q, double e)
{
	if (q>=0 && e >=0) {
		quiz = q;
		exam = e;
	}
	else {
		name = n;
		quiz = 0;
		exam = 0;
	}
}

string Student::getName()
{
	return name;
}
 
void Student::setName(string n)
{
	name = n;
}

double Student::getQuiz()
{
	return quiz;
}

void Student::setQuiz(double q)
{
	if (q <0) {
		cout << "error";
	}
	else {
		quiz = q;

	}
}

double Student::getExam()
{
	return exam;
}

void Student::setExam(double e)
{
	if (e < 0) {
		cout << "error";
	}
	else {
		exam = e;

	}

}


double Student::finalResult()
{
	return (40*quiz)/100 + (60*exam)/100;
}


