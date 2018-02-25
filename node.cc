// node.cc

#include "node.h"
#include <iostream>

Node::Node(int id){
    id_ = id;
}

Node::~Node(){

}

void Node::info(){
    std::cout << "id: " << id_ << std::endl;
}