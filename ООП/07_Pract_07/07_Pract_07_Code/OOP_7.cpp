#include "Triangle.h"
#include <iostream>
using namespace std;

int main()
{
	int choice = 1;
	while (choice)
	{

		switch (choice)
		{

			case 1:
			{
				try
				{
					Triangle triangle;
					cin >> triangle;
					triangle.Heron_formula();
					cout << triangle;
				}
				catch (Exception ex)
				{
				cout << "Error:" << ex.GET_Error() << endl;
				}
				break;
			}
			default:
			{
				cout << "Incorrect choice" << endl;

			}


		}

		cout << "\nContinue?\nYes - 1\nNo - 0" << endl;
		cin >> choice;
		cout << endl;
	}
}
