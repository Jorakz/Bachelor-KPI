#include <iostream>

using namespace std;
class PRODUCT
{
private:
    char* name;
    char* manufacturer;
    char* expiration_date;
    int quantity;
    float price;


public:

    PRODUCT (char* input_name, char* input_manufacturer, char* input_expiration_date, int input_quantily, float input_price) : name(input_name), manufacturer(input_manufacturer), expiration_date(input_expiration_date), quantity(input_quantily), price(input_price)
    {
        char name [100];
        char manufacturer[100];
        char expiration_date[100];
    }

    ~PRODUCT()
    {
        cout << " Destructor called" << endl;
    }
    char* GET_name()
    {
        return name;
    }
    char* GET_manufacturer()
    {
        return manufacturer;
    }
    char* GET_expiration_date()
    {
        return expiration_date;
    }
    int GET_quantity()
    {
        return quantity;
    }
    float GET_price()
    {
        return price;
    }


    void SET_name(char* input_name)
    {
        name = input_name;
    }
    void SET_manufacturer(char* input_manufacturer)
    {
        manufacturer = input_manufacturer;
    }
    void SET_expiration_date(char* input_expiration_date)
    {
        expiration_date = input_expiration_date;
    }
    void SET_quantity(int input_quantily)
    {
        quantity = input_quantily;
    }
    void SET_price(float input_price)
    {
        price = input_price;
    }
    void print()
    {
        cout << "Name: " << GET_name()
            << "\nManufacturer: " << GET_manufacturer()
            << "\nPrice: " << GET_price()
            << "\nExpiration_date: " << GET_expiration_date()
            << "\nQuantity: " << GET_quantity() << endl << endl;;
    }
};


int main()
{
    PRODUCT* roduct1 = new PRODUCT(0, 0, 0, 0, 0);
    char* name[100];
    char* manufacturer[100];
    char* expiration_date[100];
    float price;
    int quantity, choice = 0;
    while (choice != 8)
    {

        cout << "\nInput name - 1\nInput manufacturer - 2\nInput price - 3\nInput expiration date - 4\nInput quantity - 5\nInput all information about product - 6\nPrint information about product - 7\nExit - 8\n" << endl;
        cin >> choice;
        if (choice == 1)
        {
            cout << "Name: ";
            cin >> name;
            roduct1.SET_name(name);
        }
        else if (choice == 2)
        {
            cout << "Manufacturer: ";
            cin >> manufacturer;
            roduct1.SET_manufacturer(manufacturer);
        }
        else if (choice == 3)
        {
            cout << "Price: ";
            cin >> price;
            roduct1.SET_price(price);
        }
        else if (choice == 4)
        {
            cout << "Expiration_date: ";
            cin >> expiration_date;
            roduct1.SET_expiration_date(expiration_date);
        }
        else if (choice == 5)
        {
            cout << "Quantity: ";
            cin >> quantity;
            roduct1->SET_quantity(quantity);
        }
        else if (choice == 6)
        {
            cout << "Name: ";
            cin >> name;
            roduct1.SET_name(name);
            cout << "Manufacturer: ";
            cin >> manufacturer;
            roduct1.SET_manufacturer(manufacturer);
            cout << "Price: ";
            cin >> price;
            roduct1.SET_price(price);
            cout << "Expiration_date: ";
            cin >> expiration_date;
            roduct1.SET_expiration_date(expiration_date);
            cout << "Quantity: ";
            cin >> quantity;
            roduct1.SET_quantity(quantity);
        }
        else if (choice == 7)
        {
            roduct1->print();
        }
        else if (choice == 8)
        {
            cout << "Exit from the program " << endl;

            delete roduct1;
        }
        else
        {
            cout << "Incorrectly selected command.The number must be between 1 and 8" << endl;
        }
    }
    return 0;
}
