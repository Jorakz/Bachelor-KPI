#pragma once
#include <string>
#include <iostream>
#include <fstream>
using namespace std;
class Service_center
{
protected:
	string client = " ";
	string device = " ";
	string manufacturer = " ";
	string model;
	int date = 0; 

public:
	Service_center();
	Service_center(string c_client, string c_device, string c_manufacturer, string c_model, int c_date);
	virtual ~Service_center();

	string GET_device();
	string GET_manufacturer();
	string GET_model();
	string GET_client();
	int GET_date();
;

	void SET_divece(string device);
	void SET_manufacturer(string manufacturer);
	void SET_model(string model);
	void SET_client(string client);
	void SET_date(int date);
	virtual void print();
	virtual void input();
};

