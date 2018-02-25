// main.cc

#include <iostream>
#include "node.h"
#include "edge.h"

int id = 0;

int getId(){
    return id++;
}

int main(int argc, char *argv[]){

    Node *n1 = new Node(getId());
    Node *n2 = new Node(getId());
    n1->info();
    n2->info();
    delete n1;
    delete n2;

    Node n3(getId());
    n3.info();

    Edge e1;

    return 0;
}