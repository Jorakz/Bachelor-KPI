#include "Warranty_repair.h"








Warranty_repair::Warranty_repair(string c_client, string c_device, string c_manufacturer, string c_model, int c_date, string c_item_code, string c_problem) :Service_center(c_client, c_device, c_manufacturer ,c_model, c_date), item_code(c_item_code), problem(c_problem)
{


}

Warranty_repair::Warranty_repair()
{

}


Warranty_repair::~Warranty_repair()
{
}

void Warranty_repair::SET_item_code(string item_code)
{
	this->item_code = item_code;
}

void Warranty_repair::SET_problem(string problem)
{
	this->problem = problem;
}

string Warranty_repair::GET_problem()
{
	return problem;
}

string Warranty_repair::GET_item_code()
{
	return item_code;
}

void Warranty_repair::input()
{
	Service_center::input();
	cout << "Enter item_code: ";
	cin >> item_code;
	cout << "Enter the problem: ";
	cin >> problem;
}

void Warranty_repair::print()
{
	Service_center::print();
	cout << "\nProblem: " << problem 
		<<"\nItem code: "<< item_code << endl << endl;
}

ostream& operator<<(ostream& os, Warranty_repair& data)
{
	os << data.client << endl
		<< data.device << endl
		<< data.manufacturer << endl
		<< data.model << endl
		<< data.date << endl
		<< data.problem << endl
		<< data.item_code << endl;

	return os;
}

istream& operator>>(istream& is, Warranty_repair& data)
{
	is >> data.client >> data.device >> data.manufacturer >> data.model >> data.date >> data.problem >> data.item_code;
	return is;
}

