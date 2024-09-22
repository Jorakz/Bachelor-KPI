#include <iostream>

#include "Product.h"
using namespace std;
int main()
{
	int length = 0;
	string name;
	string manufacturer;
	int expiration_date;
	float price;
	cout << "Value of objects: ";
	cin >> length;

	//Product_array* array = new Product[length];
	Product_array array;
	for (int i = 0; i < length; i++)
	{

		array[i].print(i);
	}
	cout << "Input manufacturer: ";
	cin >> manufacturer;
	array.Cheak_manufacturer(length, manufacturer, array);
	
	cout << "Input name: ";
	cin >> name;
	cout << "Input price: ";
	cin >> price;
	array->Cheak_name_and_price(length, name, price, array);

	cout << "Input expiration date: ";
	cin >> expiration_date;
	array->Cheak_expiration_date(length, expiration_date, array);

	delete[] array;
	return 0;
}

