#include "Regulatory_service.h"

Regulatory_service::Regulatory_service(string c_client, string c_device, string c_manufacturer, string c_model, int c_date, int c_price, string c_funtion):Service_center(c_client, c_device,c_manufacturer, c_model, c_date),price(c_price), function(function)
{
	client = c_client;
	device = c_device;
	manufacturer = c_manufacturer;
	model = c_model;
	price = c_price;
	function = c_funtion;
}

Regulatory_service::Regulatory_service()
{
}

Regulatory_service::~Regulatory_service()
{
}

void Regulatory_service::SET_price(int price)
{
	this->price = price;
}

void Regulatory_service::SET_funtion(string function)
{
	this->function = function;
}

int Regulatory_service::GET_price()
{
	return price;
}

string Regulatory_service::GET_function()
{
	return function;
}

void Regulatory_service::input()
{
	Service_center::input();
	cout << "Enter price: ";
	while (price < 0)
	{
		cin >> price;
	}
	
	cout << "Enter function: ";
	cin >> function;
}

void Regulatory_service::print()
{
	Service_center::print();
	cout << "\nPrice: " << price
		<< "\nFunction: " << function << endl << endl;

}

ostream& operator<<(ostream& os, Regulatory_service& data)
{
	os << data.client << endl
		<< data.device << endl
		<< data.manufacturer << endl
		<< data.model << endl
		<< data.date << endl
		<< data.price << endl
		<< data.function << endl;


	return os;
}

istream& operator>>(istream& is, Regulatory_service& data)
{
	is >> data.client >> data.device >> data.manufacturer >> data.model >> data.date >>data.price >> data.function;
	return is;
}

