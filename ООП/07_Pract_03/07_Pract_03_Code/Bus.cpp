#include "Bus.h"

void Bus::print()
{ 
	cout << "______________" << endl;
	cout << "TRUCK INFO" <<
		"\nName: " << name <<
		"\nManufacturer: " << manufacturer <<
		"\nMax speed: " << speed <<
		"\nPlace: " << place << endl;
	cout << "______________" << endl << endl;;
}

Bus::Bus(string name, string manufacturer, int speed, int place)
{ 
	this->name = name;
	this->manufacturer = manufacturer;
	this->speed = speed;
	this->place = place;
}

Bus::~Bus()
{
}
