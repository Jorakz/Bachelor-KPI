#pragma once
#include <iostream>
#include <string>
#include "Node.h"
using namespace std;
template<typename T>

class List
{
private:
    int size;

    Node<T>* head;
public:
    ~List();
    List();
    void push_back(T data);
    int get_size();
    T& operator[](const int id);
    void print_list();
    void cheak_empty();
    void clean_list();
    void delete_element(int id);
};

template<typename T>
inline List<T>::~List()
{

}

template<typename T>
inline List<T>::List()
{
    size = 0;
    head = nullptr;
}

template<typename T>
inline void List<T>::push_back(T data)
{
    if (head == nullptr)
    {
        head = new Node<T>(data);
    }
    else
    {
        Node<T>* current = this->head;
        while (current->pNext != nullptr)
        {
            current = current->pNext;
        }
        current->pNext = new Node<T>(data);
    }
    size++;

}



template<typename T>
int List<T>::get_size()
{
    return size;
}

template<typename T>
inline T& List<T>::operator[](const int id)
{
    int count = 0;
    Node<T>* current = this->head;
    while (current != nullptr)
    {
        if (count == id)
        {

            return current->data;
        }
        current = current->pNext;
        count++;
    }


}

template<typename T>
inline void List<T>::print_list()
{
    for (int i = 0; i < size; ++i)
    {
        cout << operator[](i)<< " -> ";
    }
    
    cout <<"NULL"<< endl;
}

template<typename T>
inline void List<T>::cheak_empty()
{
    if ((get_size()) == 0)
    {
        cout << "The list is empty" << endl;;
    }
    else
    {
        cout << "The list is not empty" << endl;
    }
}

template<typename T>
inline void List<T>::clean_list()
{
    while (size)
    {
        Node <T> *temp = head;
        head = head->pNext;
        delete temp;
        --size;
    }
}

template<typename T>
inline void List<T>::delete_element(int id)
{
 
    Node<T>* current = this->head;
    int count = 0;
    int i = 0;
    id--;
    while (current != nullptr && i!=1)
    {
        if (id == -1)
        {
            Node <T>* temp = head;
            head = head->pNext;
            delete temp;
            i++;
            size--;
        }
        else if(count == id)
        {
            Node<T>* temp = current->pNext;
            current->pNext = temp->pNext;
            delete temp;
            size--;
            i++;
        }
        current = current->pNext;
        count++;
    }
    
}
