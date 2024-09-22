#include "Service_center.h"

Service_center::Service_center()
{
}

Service_center::Service_center(string c_client, string c_device, string c_manufacturer, string c_model, int c_date):client(c_client), device(c_device), manufacturer(c_manufacturer), model(c_model), date(c_date)
{


}

Service_center::~Service_center()
{
}

string Service_center::GET_device()
{
	return device;
}

string Service_center::GET_manufacturer()
{
	return manufacturer;
}

string Service_center::GET_model()
{
	return model;
}

string Service_center::GET_client()
{
	return client;
}

int Service_center::GET_date()
{
	return date;
}


void Service_center::SET_divece(string device)
{
	this->device = device;
}

void Service_center::SET_manufacturer(string manufacturer)
{
	this->manufacturer = manufacturer;
}

void Service_center::SET_model(string model)
{
	this->model = model;
}

void Service_center::SET_client(string client)
{
	this->client = client;
}

void Service_center::SET_date(int date)
{
	this->date = date;
}

void Service_center::print()
{
	cout << "Client: " << client
		<< "\nDevice:  " << device
		<< "\nManufacturer: " << manufacturer
		<< "\nModel:: " << model
		<< "\nDate: " << date;
}

void Service_center::input()
{

	cout << "Enter client name: ";
	cin >> client;
	cout << "Enter divece: ";
	cin >> device;
	cout << "Enter manufacturer: ";
	cin >> manufacturer;
	cout << "Enter model: ";
	cin >> model;
	cout << "Enter date: ";
	while (date <= 0)
	{
		cin >> date;
	}


}



