#include "Main.h"

#include <iostream>
#include <string>
using namespace std;

void Regulatory_service_q(Priority_queue*& P_q)
{
	system("cls");
	Regulatory_service* info = new Regulatory_service();
	int priority = 0;
	info->input();
	while (priority <= 0)
	{
		cout << "Enter priority: ";
		cin >> priority;
	}
	P_q->insert_q(info, priority);
	system("pause");
	system("cls");
}
void Warranty_repair_q(Priority_queue*& P_q)
{
	system("cls");
	Warranty_repair* info = new Warranty_repair();
	int priority = 0;
	info->input();
	while (priority <= 0)
	{
		cout << "Enter priority: ";
		cin >> priority;
	}
	P_q->insert_q(info, priority);
	system("pause");
	system("cls");
}
void Delete_object(Priority_queue*& P_q)
{
	system("cls");
	P_q->delete_q();
	system("pause");
	system("cls");
}
void Delete_all_object(Priority_queue*& P_q)
{
	system("cls");
	P_q->delete_all_q();
	cout << "The priority queue has been cleared" << endl;
	system("pause");
	system("cls");
}
void Print_object(Priority_queue*& P_q)
{
	system("cls");
	P_q->print_q();
	system("pause");
	system("cls");
}
void Save_object(Priority_queue*& P_q)
{
	system("cls");
	P_q->input_in_file();
	system("pause");
	system("cls");
}
void Load_object(Priority_queue*& P_q)
{
	system("cls");
	P_q->delete_all_q();
	P_q->output_from_file();
	system("pause");
	system("cls");
}
void Count(Priority_queue*& P_q)
{
	system("cls");
	P_q->count_in_q();
	system("pause");
	system("cls");
}
int main()
{
	Priority_queue* P_q = new Priority_queue;
	int choice;
	string cheak_choice;
	do
	{
		cout << "SELECT FUNCTION:" <<
			"\n\t<1> - Create regulatory maintenance of equipment" <<
			"\n\t<2> - Create warranty repair of equipment" <<
			"\n\t<3> - Delete the object" <<
			"\n\t<4> - Delete the priority queue" <<
			"\n\t<5> - Print priority queue" <<
			"\n\t<6> - Save priority queue in file" <<
			"\n\t<7> - Load priority queue from file" <<
			"\n\t<8> - Count the number of equipment and given by the manufacturer" <<
			"\n\t<9> - Exit" << endl << endl;

		try
		{
			cin >> choice;
		}
		catch (const exception&)
		{
			cout << "Incorrect data entry, try again" << endl;
			system("pause");
			system("cls");
		}
		switch (choice)
		{
		case 1:
		{
			Regulatory_service_q(P_q);
			break;
		}
		case 2:
		{
			Warranty_repair_q(P_q);
			break;
		}
		case 3:
		{
			Delete_object(P_q);
			break;
		}
		case 4:
		{
			Delete_all_object(P_q);
			break;
		}
		case 5:
		{
			Print_object(P_q);
			break;
		}
		case 6:
		{
			Save_object(P_q);
			break;
		}
		case 7:
		{
			Load_object(P_q);
			break;
		}
		case 8:
		{
			Count(P_q);
			break;
		}
		case 9:
		{
			break;
		}
		default:
		{
			system("cls");
			cout << "There are no functions under this number, try again" << endl;
			system("pause");

			
			break;
		}

		}
	} while (choice != 9);

	return 0;
	
}

Main::Main()
{

}

Main::~Main()
{
	P_q->delete_all_q();
}





