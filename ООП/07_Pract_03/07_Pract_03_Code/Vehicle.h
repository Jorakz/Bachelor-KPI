#pragma once
#include <iostream>
#include <string>
using namespace std;

class Vehicle
{
protected:
	string name;
	string manufacturer;
	int speed;
public:
	Vehicle();
	~Vehicle();
	void SET_name(string name);
	void SET_manufacturer(string manufacturer);
	void SET_speed(int speed);
	virtual void print();
};

