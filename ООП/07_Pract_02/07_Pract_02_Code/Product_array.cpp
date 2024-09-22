#include "Product_array.h"
#include <string>
#include <iostream>
using namespace std;
Product_array::Product_array(int len)
{
	array = new Product * [len];
	
}

Product_array::~Product_array()
{
	delete[] array;
}

void Product_array::Cheak_manufacturer(int length, string manufacturer, Product_array* array)
{
	for (int j = 0; j < length; j++)
	{
		if (manufacturer == GET_manufacturer(array[j]))
		{
			cout << endl;
			array[j].print(j);

		}
	}
}

void Product_array::Cheak_name_and_price(int length, string name, float price, Product_array* array)
{
	for (int j = 0; j < length; j++)
	{
		if (name == GET_name(array[j]) && price >= GET_price(array[j]))
		{
			cout << endl;
			array[j].print(j);

		}
	}
}

void Product_array::Cheak_expiration_date(int length, int expiration_date, Product_array* array)
{
	for (int j = 0; j < length; j++)
	{
		if (expiration_date <= GET_expiration_date(array[j]))
		{
			cout << endl;
			array[j].print(j);

		}
	}
}



