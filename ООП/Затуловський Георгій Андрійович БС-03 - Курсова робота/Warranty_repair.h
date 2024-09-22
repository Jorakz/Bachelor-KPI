#pragma once
#include "Service_center.h"

class Warranty_repair : public Service_center
{
	
private:
	string item_code;
	string problem;
public:
	Warranty_repair(string c_client, string c_device, string c_manufacturer, string c_model, int c_date, string c_item_code, string c_problem);
	Warranty_repair();
	~Warranty_repair();
	void SET_item_code(string item_code);
	void SET_problem(string problem);
	string GET_problem();
	string GET_item_code();

	void input();
	void print();
	friend ostream &operator<<(ostream& os, Warranty_repair& data);
	friend istream &operator>>(istream& is, Warranty_repair& data);
};

