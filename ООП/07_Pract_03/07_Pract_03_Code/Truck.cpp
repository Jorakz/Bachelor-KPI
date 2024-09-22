#include "Truck.h"

void Truck::print()
{
	cout << "______________" << endl;
	cout << "TRUCK INFO" <<
		"\nName: " << name <<
		"\nManufacturer: " << manufacturer <<
		"\nMax speed: " << speed << 
		"\nLoad capacity: " << load_capacity << " kg "<<endl;
	cout << "______________" << endl << endl;;
}

Truck::Truck(string name, string manufacturer, int speed, float load_capacity)
{
	this->name= name;
	this->manufacturer= manufacturer;
	this->speed= speed;
	this->load_capacity = load_capacity;
}

Truck::~Truck()
{
}
