#pragma once
#include <math.h>
#include <iostream>
#include <string>
#include "Exception.h"
using namespace std;
class Triangle
{
private:
	double AB;
	double BC;
	double AC;
	double S;
public:
	Triangle();
	~Triangle();
	friend ostream& operator<< (ostream &out, const Triangle &Triangle);
	friend istream& operator>> (istream & out, Triangle &Triangle);
	void Heron_formula();

};

