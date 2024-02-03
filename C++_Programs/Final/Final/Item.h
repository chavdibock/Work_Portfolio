#pragma once
#include<iostream>
#include<string>
using namespace std;
class Item {
public:
    bool operator<(const Item& itm) const;
private:
    string id;
    string name;
    float* price;
};