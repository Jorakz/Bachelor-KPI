#include <iostream>
#include "Vehicle.h"
#include "Bus.h"
#include "Truck.h"
#include <string>
using namespace std;

void CREATE_VEHICLE()
{
	string name = "";
	string manufacturer = "";
	int speed = 0;
	int choice = 0;
	cout << "Choice type of vehicle: \n"
		<< "Bus - 1\n"
		<< "Truck - 2" << endl << endl;
	while (choice != 1 && choice != 2)
	{
		cin >> choice;
	}
	
	Vehicle veh;
	cout << "Name: ";
	cin >> name;
	veh.SET_name(name);
	cout << "Manufacturer: ";
	cin >> manufacturer;
	veh.SET_manufacturer(manufacturer);
	cout << "Max speed: ";
	cin >> speed;
	veh.SET_speed(speed);

	
	veh.print();
	

	if (choice == 1) 
	{
	
		int place = 0;
		cout << "Place: ";
		cin >> place;
		Bus veh(name, manufacturer, speed, place);
		veh.print();
	}
	else
	{

		float load_capacity = 0;
		cout << "Load capacity (kg): ";
		cin >> load_capacity;
		Truck veh(name, manufacturer, speed, load_capacity);
		veh.print();
	}

	cout << "Restart the program?\nYes - 1\nNo - 2\n";
	cin >> choice;
	if (choice == 1)
	{
		cout << endl << endl;
		CREATE_VEHICLE();
	}
	else
	{
		cout << "Closing the program" << endl;
	}
}

int main()
{
	CREATE_VEHICLE();
	return 0;
}

