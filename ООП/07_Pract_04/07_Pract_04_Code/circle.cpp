#include "circle.h"
#include <math.h>
circle::circle(double rad, int x, int y)
{
	this->rad = rad;
	this->x = x;
	this->y = y;
}

circle::circle()
{
	rad = x = y = 0;
}

circle::~circle()
{
}

double circle::length()
{
	double pi = 3.14;
	return (rad*pi*2);
}

double circle::area()
{
	double pi = 3.14;
	return (rad * pow(pi,2));
}

void circle::SET_rad(double rad)
{
	this->rad = rad;
}

void circle::SET_x(int x)
{
	this->x = x;
}

void circle::SET_y(int y)
{
	this->y = y;
}

double circle::GET_rad()
{
	return rad;
}

int circle::GET_x()
{
	return x;
}

int circle::GET_y()
{
	return y;
}

void circle::print()
{
	cout << "Circle center coordinates: [" << x << " ; " << y << "]\n"
		<< "r = " << rad << " cm\n"
		<< "l = " << length() << " cm\n"
		<< "S = " << area() << " cm\n"
		<<endl;
}

bool circle::operator==(const circle& cheak)
{
	return (this->rad == cheak.rad);
}

bool circle::operator!=(const circle& cheak)
{
	return (this->rad == cheak.rad);
}

bool circle::operator<(const circle& cheak)
{
	return (this->rad < cheak.rad);
}

bool circle::operator>(const circle& cheak)
{
	return (this->rad > cheak.rad);
}

bool circle::operator<=(const circle& cheak)
{
	return (this->rad <= cheak.rad);
}

bool circle::operator>=(const circle& cheak)
{
	return (this->rad >= cheak.rad);
}

circle& circle::operator++()
{
	this->x++;
	this->y++;
	this->rad++;
	return *this;
}

circle& circle::operator--()
{
	this->x--;
	this->y--;
	this->rad--;
	return *this;
}
