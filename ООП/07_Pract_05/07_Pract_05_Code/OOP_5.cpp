#include "List.h"
#include <iostream>
#include <string>
using namespace std;
//template<typename T>
int main()
{
    List<int> lst;
    bool prog = true;
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
            lst.cheak_empty();

            break;
        case 2:
            cout << "List size: " << (lst.get_size()) << endl;
            break;
        case 3:
            cout << "Current index: ";
            cin >> input;
            cout<<"Current element: " << lst[input] << endl;
            break;
        case 4:
            cout << "Input data: ";
            cin >> input;
            lst.push_back(input);

            break;
        case 5:
            cout << "Input index of element wich you want delete: ";
            input =(lst.get_size()+1);
            while (input > lst.get_size() && lst.get_size() != 0)
            {
                cin >> input;
                lst.delete_element(input);
            }

            break;
        case 6:
            lst.clean_list();
            cout << "List cleared" << endl;
            break;
        case 7:
            lst.print_list();
            break;
        case 8:
            lst.clean_list();
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

