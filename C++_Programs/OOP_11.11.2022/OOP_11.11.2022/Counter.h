#pragma once
using namespace std;

class Counter
{
public:

	Counter();
	int getCount();
	int getMaxValue();
	void setCount(int);
	void setMaxValue(int);
	void increment();
	void decrement();


private:
	int count, maxValue;

};

