#pragma once
#include <iostream>
#include <string>
#include "Vehicle.h"
using namespace std;

class Bus : public Vehicle
{
protected:
	int place;
public:
	void print() override;
	Bus(string name, string manufacturer, int speed, int place);
	~Bus();

};

