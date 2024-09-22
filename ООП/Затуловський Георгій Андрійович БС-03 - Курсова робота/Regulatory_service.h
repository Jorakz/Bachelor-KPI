#pragma once
#include "Service_center.h"
class Regulatory_service: public Service_center
{
private:
	int price;
	string function;
public:
	Regulatory_service(string c_client, string c_device, string c_manufacturer, string c_model, int c_date, int c_price, string c_function);
	Regulatory_service();
	~Regulatory_service();
	void SET_price(int price);
	void SET_funtion(string function);
	int GET_price();
	string GET_function();
	void input();
	void print();
	friend ostream& operator<<(ostream& os, Regulatory_service& data);
	friend istream& operator>>(istream& is, Regulatory_service& data);
};

