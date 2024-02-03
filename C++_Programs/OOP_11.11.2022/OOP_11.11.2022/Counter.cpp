#include "Counter.h"
#include <iostream>
using namespace std;
Counter::Counter()
{
	int count = 0;
	int maxValue = 100;

}

int Counter::getCount() {
	return count;
}

int Counter::getMaxValue()
{
	return maxValue;
}

void Counter::setCount(int c)
{
	if (c > 0) {
		count = c;
	}
	else {
		count = 0;
	}
}

void Counter::setMaxValue(int m)
{
	if (m > 0) {
		maxValue = m;
	}
	else {
		maxValue = 100;
	}
}

void Counter::increment()
{
	if (count >= maxValue) {
		cout << " error" << endl;
	}
	else {
		count++;

	}
}

void Counter::decrement()
{
	if (count <= 0) {
		cout << " error" << endl;
	}
	else {
		count--;

	}

}


