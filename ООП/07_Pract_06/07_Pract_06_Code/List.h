#pragma once
#include <iostream>
#include <string>
#include <forward_list>
#include <iterator>
using namespace std;
template<typename T>
class List 
{
private:
	forward_list<T> Node;
	int size;
public:
	List();
	~List();
	bool empty_list();
	int size_list();
	void find_in_list(int input);
	void input_in_list(int input);
	void clean_list();
	void print_lise();
	void delete_elem_in_list(int id);
};

template<typename T>
inline List<T>::~List()
{
	
}

template<typename T>
inline bool List<T>::empty_list()
{
	if (Node.empty() == false)
	{
		return false;
	}
		
	else
	{
		return true;
	}

}

template<typename T>
inline int List<T>::size_list()
{
	return size;
}

template<typename T>
inline void List<T>::find_in_list(int input)
{
	if (size > input)
	{
		forward_list<int>::iterator it = Node.begin();
		for (int i = 0; i < input; i++, it++)
		{
			if (i == input)
			{
				cout << "Current element: " << *it << endl;
			}
		}
	}


}

template<typename T>
inline void List<T>::input_in_list(int input)
{
	typename forward_list<T>::iterator it = Node.begin();
	if (size == 0) 
	{
		Node.push_front(input);
	}
	else
	{
		for (int i = 0; i <= size; i++, it++)
		{

			if (size-1 == i)
			{
				Node.emplace_after(it, input);

			}
		}
	}
	size++;

}

template<typename T>
inline void List<T>::clean_list()
{
	Node.clear();
	size = 0;
}

template<typename T>
inline void List<T>::print_lise()
{
	for (auto elem : Node)
	{
		cout << elem << " -> ";
	}
	cout << "NULL" << endl;
}

template<typename T>
inline void List<T>::delete_elem_in_list(int id)
{
	if (size >= 1 && id == 0)
	{
		Node.pop_front();
		size--;
	}
	if (id < size && id != 0)
	{

		typename forward_list<T>::iterator it = Node.begin();

		for (int i = 0; i < id; i++, it++)
		{

			if (id - 1 == i)
			{
				Node.erase_after(it);
				size--;
			}
		}
		
	}

	
}

template<typename T>
inline List<T>::List()
{
	size = 0;
}



