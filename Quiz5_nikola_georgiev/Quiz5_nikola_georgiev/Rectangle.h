#pragma once
class Rectangle
{
public:
	Rectangle();
	Rectangle(int, int);
	int getHeight();
	int getWidth();
	void setHeight(int);
	void setwidht(int);
	int getAera();
private:
	int height;
	int width;
};