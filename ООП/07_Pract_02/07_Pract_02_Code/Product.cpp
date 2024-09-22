#include "Product.h"

#include <iostream>
#include <string>
using namespace std;

Product::Product(string name, string manufacturer, int expiration_date, int quantity, int price)
{
	this->name = name;
	this->manufacturer = manufacturer;
	this->expiration_date = expiration_date;
	this->quantity = quantity;
	this->price = price;

}

Product::Product()
{

	string choise_name[5] = { "Licorice","Chocolate","Hard_Candies","Lollipops","Caramels" };
	string choise_manufacturer[5] = { "Roshen","Ferrero","Hershey","Nestle","Meiji" };

	name = choise_name[rand() % 5];
	manufacturer = choise_manufacturer[rand() % 5];
	expiration_date = 15 + rand() % 345;
	quantity = rand() % 1000;
	price = 14 + rand() % 100;
}

Product::~Product()
{
}

void Product::print(int number)
{
	int cheak_number = 0;

	cout << "#" << number + 1 << endl
		<< "Name: " << name
		<< "\nManufacturer: " << manufacturer
		<< "\nPrice: " << to_string(price)
		<< "\nExpiration_date: " << to_string(expiration_date)
		<< "\nQuantity: " << to_string(quantity) << endl << endl;
}

string Product_array::GET_name(Product_array x)
{

	return x.name;
}
string Product_array::GET_manufacturer(Product_array x)
{
	return x.manufacturer;
}
int Product_array::GET_expiration_date(Product_array x)
{
	return x.expiration_date;
}

float Product_array::GET_price(Product_array x)
{
	return x.price;
}
