#pragma once
#include <iostream>
#include <string>
#include "Vehicle.h"
using namespace std;
class Truck : public Vehicle
{
protected:
	float load_capacity;
public:
	void print() override;
	Truck(string name, string manufacturer, int speed, float load_capacity);
	~Truck();
};

