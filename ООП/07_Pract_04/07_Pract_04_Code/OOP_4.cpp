#include "circle.h"
#include <string>
#include <iostream>
using namespace std;
void Cheak(circle& A, circle& B)
{
	cout << "=================\nr - radius" << endl;
	cout << "r(A) == r(B) = " << (A == B) << endl;
	cout << "r(A) != r(B) = " << (A != B) << endl;
	cout << "r(A) >  r(B) = " << (A > B) << endl;
	cout << "r(A) >= r(B) = " << (A >= B) << endl;
	cout << "r(A) <  r(B) = " << (A < B) << endl;
	cout << "r(A) <= r(B) = " << (A <= B) << endl;
	cout << "=================" << endl;
}
void working_with_circle()
{
	int x = 0, y = 0;
	double rad = 0;
	
	cout << "Input circle A center coordinates: x = ";
	cin >> x;
	cout << "Input circle A center coordinates: y = ";
	cin >> y;
	cout << "Input radius A: ";

	while (rad <= 0)
	{
		cin >> rad;
	}
	circle A(rad, x, y);
	rad = 0;
	cout << "\nCircle A" << endl;
	A.print();

	cout << "Input circle B center coordinates: x = ";
	cin >> x;
	cout << "Input circle B center coordinates: y = ";
	cin >> y;
	cout << "Input radius B: ";

	while (rad <= 0)
	{
		cin >> rad;
	}
	circle B(rad,x, y);
	rad = 0;
	cout << "\nCircle B" << endl;
	B.print();
	Cheak(A,B);

	A.operator--();
	B.operator++();
	cout << "\nCircle A after - 1" << endl;
	A.print();
	cout << "\nCircle B after + 1" << endl;
	B.print();
	Cheak(A, B);
}

int main()
{
	working_with_circle();
}
