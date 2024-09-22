#include "Priority_queue.h"


Priority_queue::Priority_queue()
{
}

Priority_queue::~Priority_queue()
{
}

void Priority_queue::insert_q(Service_center* item, int priority)
{
	Node* tmp, * pBack;
	tmp = new Node;
	tmp->data = item;
	tmp->priority = priority;
	if (node == NULL || priority <= node->priority)
	{
		tmp->pNext = node;
		node = tmp;
	}
	else
	{
		pBack = node;
		while (pBack->pNext != NULL && pBack->pNext->priority)
		{
			pBack = pBack->pNext;
		}
		tmp->pNext = pBack->pNext;
		pBack->pNext = tmp;
	}

}

void Priority_queue::delete_q()
{
	Node *tmp;
	if (node == NULL)
	{
		cout << "Priority queue is clear" << endl;

	}
	else
	{
		tmp = node;
		
		cout << "Deleted item is \n\n";
		tmp->data->print();
		node = node->pNext;
		free(tmp);
	}
}

void Priority_queue::print_q()
{
	Node* ptr = node;
	if (node == NULL)
		cout <<"Priority queue is empty "<< endl;
	else
	{
		cout << "Priority queue is: " << endl;
		
		while (ptr != NULL)
		{
			Service_center* Data_info = ptr->data;
			cout <<"Priority:"<< ptr->priority<< endl;
			Data_info->print();

			ptr = ptr->pNext;
		}
	}
}

void Priority_queue::delete_all_q()
{
	Node* tmp;
	while (node != NULL)
	{

		tmp = node;
		node = node->pNext;
		free(tmp);

	}

}


void Priority_queue::count_in_q()
{
	int count = 0;
	Node* tmp = node;
	string find_manufacturer = " ";
	cout << "Enter manufacturer name: ";
	cin >> find_manufacturer;
	while (tmp != NULL)
	{
	
		if (typeid(*(tmp->data)) == typeid(Warranty_repair) && (tmp->data)->GET_manufacturer() == find_manufacturer)

		{
			count++;
		}
		tmp = tmp->pNext;

	}
	cout << "The total count of warranty repairs of equipment and manufacturer name "<< find_manufacturer<<": " << count << endl;



}

void Priority_queue::input_in_file()
{
	Node* ptr = node;
	if (ptr != NULL)
	{
		string path;
		cout << "Enter file name: ";
		cin >> path;
		ofstream fout;
		fout.open(path);
		if (!fout.is_open())
		{
			cout << "File opening error. Exit to main menu" << endl;
			return;
		}

		while (ptr != NULL)
		{
			if (typeid(*(ptr->data)) == typeid(Regulatory_service))
			{
				fout << "Regulatory_service" << endl;
				fout << (ptr->priority)<<endl;
				fout << (*((Regulatory_service*)(ptr->data)));
			}
			else
			{
				fout << "Warranty_repair"<<endl;
				fout << (ptr->priority) << endl;
				fout << (*((Warranty_repair*)(ptr->data)));
			}
			ptr = ptr->pNext;
			fout << endl;
		}
		fout.close();
		cout << "Writing to file is completed!" << endl;
	}
	
}

void Priority_queue::output_from_file()
{

	string path = " ";
	cout << "Enter path to file: ";
	cin >> path;
	ifstream fin;
	fin.open(path);
	if (!fin.is_open())
	{
		cout << "File opening error. Exit to main menu" << endl;
		return;
	}
	else
	{
		
		string type;
		int priority_file = 0;
		char cheak;
		while (!fin.eof())
		{
			fin >> type;
			fin >> priority_file;
			if (type == "Regulatory_service")
			{
				Regulatory_service* R_s_file = new Regulatory_service;
				fin >> *(R_s_file);
				insert_q(R_s_file, priority_file);
			}
			else if(type == "Warranty_repair")
			{
				Warranty_repair* W_r_file = new Warranty_repair;
				fin >> *(W_r_file);
				insert_q(W_r_file, priority_file);
			}
			type = "";
		}
		fin.close();
		cout << "Reading from file is completed!" << endl;
		return;
	}
}
