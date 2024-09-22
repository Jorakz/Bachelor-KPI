#pragma once
#include <iostream>
#include <string>
using namespace std;
template<typename T>
class Node
{
private:

public:
	Node* pNext;
	T data;
	Node(T data, Node* pNext = nullptr);
	~Node();


};

template<typename T>
inline Node<T>::Node(T data, Node* pNext)
{
	this->data = data;
	this->pNext = pNext;
}

template<typename T>
inline Node<T>::~Node()
{

}