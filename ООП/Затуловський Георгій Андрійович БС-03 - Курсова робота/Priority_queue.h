#pragma once

#include <iostream>
#include <string>
#include <typeinfo>
#include "Service_center.h"
#include "Regulatory_service.h"
#include "Warranty_repair.h"
using namespace std;

struct Node
{
    Service_center* data;
    struct Node* pNext;
    int priority;
    
    
};

class Priority_queue
{
private:
    Node* node = NULL;
public:
    Priority_queue();
    ~Priority_queue();
    void insert_q(Service_center* item, int priority);
    void delete_q();
    void print_q();
    void delete_all_q();
    void count_in_q();
    void input_in_file();
    void output_from_file();
   
};


