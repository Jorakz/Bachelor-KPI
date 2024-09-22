#pragma once
#include <string>
#include <iostream>
using namespace std;
class circle
{
private:
	double rad;
	int x;
	int y;

public:
	circle(double rad, int x, int y);
	circle();
	~circle();
	double length();
	double area();
	void SET_rad(double rad);
	void SET_x(int x);
	void SET_y(int y);
	double GET_rad();
	int GET_x();
	int GET_y();
	void print();
	bool operator == (const circle & cheak);
	bool operator != (const circle& cheak);
	bool operator < (const circle& cheak);
	bool operator > (const circle& cheak);
	bool operator <= (const circle& cheak);
	bool operator >= (const circle& cheak);
	circle& operator ++();
	circle& operator --();
};

