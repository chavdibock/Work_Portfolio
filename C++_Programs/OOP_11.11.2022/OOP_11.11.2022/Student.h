#pragma once
#include <iostream>
#include <string>
using namespace std;
class Student
{
public:
	Student();
	Student(string, double, double);
	string getName();
	void setName(string);
	double getQuiz();
	void setQuiz(double);
	double getExam();
	void setExam(double);
	double finalResult();
private:
	string name;
	double quiz;
	double exam;
};
