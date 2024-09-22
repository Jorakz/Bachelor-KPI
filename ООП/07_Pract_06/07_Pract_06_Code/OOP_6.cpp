#include "List.h"
#include <iostream>
#include <string>
using namespace std;

int main()
{
    List<int> lst;
    bool prog = true;
    bool emp = false;
    int choice = 1;
    int input = 0;
    cout << "1 - check for emptiness\n"
        << "2 - size list\n"
        << "3 - return the current element\n"
        << "4 - add new element\n"
        << "5 - delete element\n"
        << "6 - clean list\n"
        << "7 - print list\n"
        << "8 - exit\n" << endl;
    while (prog)
    {
        cin >> choice;

        switch (choice)
        {
        case 1:
           
            emp = lst.empty_list();
            if (emp)
            {
                cout << "List is empty" << endl;
            }
            else
            {
                cout << "List is not empty" << endl;
            }
            break;
        case 2:
            cout << "List size: " << lst.size_list() << endl;
            break;
        case 3:
            cout << "Current index: ";
            cin >> input;
            lst.find_in_list(input);
            break;
        case 4:
            cout << "Input data: ";
            cin >> input;
            lst.input_in_list(input);
            break;
        case 5:
            cout << "Input index of element wich you want delete: ";
            cin >> input;
            lst.delete_elem_in_list(input);
            break;
        case 6:
            lst.clean_list();
            cout << "List cleared" << endl;
            break;
        case 7:
            lst.print_lise();
            break;
        case 8:
            cout << "Exit..." << endl;
            prog = false;
            break;
        default:
            cout << "Anoun command" << endl;
            break;
        }
    }
    return 0;
}
