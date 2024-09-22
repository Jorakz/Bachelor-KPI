#include <iostream>
#include "Product.h"

using namespace std;
class Product_array
{
private:
	Product ** array;

public:
	Product_array(int len);
	~Product_array();
    void print(int length);
    void Cheak_manufacturer(int length, string manufacturer, Product_array* array);
    void Cheak_name_and_price(int length, string name, float price, Product_array* array);
    void Cheak_expiration_date(int length, int expiration_date, Product_array* array);
    string GET_name(Product_array x);
    string GET_manufacturer(Product_array x);
    int GET_expiration_date(Product_array x);
    float GET_price(Product_array x);
    void print(int length);

};