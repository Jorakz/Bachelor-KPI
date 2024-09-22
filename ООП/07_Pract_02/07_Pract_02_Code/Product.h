#pragma once
#include <iostream>
#include "Product_array.h"
using namespace std;
class Product
{
private:
    string name;
    string manufacturer;
    int expiration_date;
    int quantity;
    int price;

public:
    Product(string name, string manufacturer, int expiration_date, int quantity, int price);
    Product();
    ~Product();

    string GET_name(Product_array x);
    string GET_manufacturer(Product_array x);
    int GET_expiration_date(Product_array x);
    float GET_price(Product_array x);
    void print(int length);


};
