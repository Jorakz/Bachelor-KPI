#include "Triangle.h"
#include "Exception.h"
#include <math.h>
Triangle::Triangle()
{
	AB = BC = AC = S = 0;
}

Triangle::~Triangle()
{
}

void Triangle::Heron_formula()
{
	if (AC > (BC + AB))
	{
		throw Exception("Incorrect input: AC > BC + AB");
	}

	double p = (AC + BC + AB) / 2;
	cout << "p = " << p << endl;
	if (AC >= p || BC >= p || AB >= p)
	{
		if(AC > p)
		{
			throw Exception("Incorrect data: AC >= p");
		}
		else if(BC > p)
		{
			throw Exception("Incorrect data: BC >= p");
		}
		else
		{
			throw Exception("Incorrect data: AB >= p");
		}
	}
	S = sqrt(p * (p - AC) * (p - BC) * (p - AB));

}

ostream& operator<<(ostream& out, const Triangle& Triangle)
{

	cout << "S = " << Triangle.S << endl;
	return out;
}

istream& operator>>(istream& out, Triangle& Triangle)
{
	cout << "Input AB:";
	cin >> Triangle.AB;
	cout << "Input BC:";
	cin >> Triangle.BC;
	cout << "Input AC:";
	cin >> Triangle.AC;
	return out;

}
