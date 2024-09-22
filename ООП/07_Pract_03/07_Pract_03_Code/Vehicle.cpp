#include "Vehicle.h"
#include <iostream>
#include <string>
using namespace std;
Vehicle::Vehicle()
{
	name ="";
	manufacturer ="";
	speed = 0;
}

Vehicle::~Vehicle()
{
}

void Vehicle::SET_name(string name)
{
	this->name = name;
}

void Vehicle::SET_manufacturer(string manufacturer)
{
	this->manufacturer = manufacturer;
}

void Vehicle::SET_speed(int speed)
{
	this->speed = speed;
}



void Vehicle::print()
{
	cout << "______________" << endl;
	cout << "VEHICLE INFO" <<
		"\nName: "<< name <<
		"\nManufacturer: " << manufacturer <<
		"\nMax speed: "<<speed << endl << endl;
	cout << "______________" << endl;
}
