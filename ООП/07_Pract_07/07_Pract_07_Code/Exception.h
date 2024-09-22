#pragma once
#include <math.h>
#include <iostream>
#include <string>

using namespace std;
class Exception
{
private:
	string Error;
public:
	Exception();
	Exception(string Error);
	~Exception();
	string GET_Error();
	void SET_Error(string Error);
};

inline Exception::Exception()
{
}

inline Exception::Exception(string Error)
{
	this->Error = Error;
}

inline Exception::~Exception()
{
}

inline string Exception::GET_Error()
{
	return Error;
}
inline void Exception::SET_Error(string Error)
{
	this->Error = Error;
}
